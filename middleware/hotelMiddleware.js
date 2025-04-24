/**
 * Hotel middleware - isteklerde otel kimliğini belirler
 * İki mod destekler:
 * 1. Sabit mod: process.env.ACTIVE_HOTEL_ID kullanır (tek instance, tek otel için)
 * 2. Dinamik mod: Host başlığı (subdomain) veya istek parametresiyle otel belirleme
 */

const determineHotelId = (req, res, next) => {
  let hotelId;

  // Öncelik sırası: 
  // 1. URL query parametresi (?hotelId=hotel1)
  // 2. Request header (X-Hotel-ID)
  // 3. Subdomain (hotel1.example.com)
  // 4. Environment variable'dan varsayılan değer
  
  if (req.query.hotelId) {
    hotelId = req.query.hotelId;
  } else if (req.headers['x-hotel-id']) {
    hotelId = req.headers['x-hotel-id'];
  } else if (req.hostname) {
    // hotel1.example.com -> hotel1
    const subdomain = req.hostname.split('.')[0];
    if (subdomain !== 'www' && subdomain !== 'api') {
      hotelId = subdomain;
    }
  }

  // Eğer yukarıdakilerden hiçbiri yoksa, varsayılan değeri kullan
  if (!hotelId) {
    hotelId = process.env.ACTIVE_HOTEL_ID || 'hotel1';
  }

  // Request nesnesine hotelId ekle, tüm route'larda kullanılabilir
  req.hotelId = hotelId;
  
  next();
};

module.exports = determineHotelId; 