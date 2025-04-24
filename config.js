const dotenv = require('dotenv');
dotenv.config();

// Otel kimliğine göre MongoDB bağlantısını belirlemek için fonksiyon
const getMongoDBConnectionString = (hotelId) => {
  const connections = {
    // Her otelin MongoDB bağlantı bilgileri
    'hotel1': process.env.MONGODB_URI_HOTEL1 || 'mongodb+srv://user:pass@cluster.mongodb.net/Hotel1',
    'hotel2': process.env.MONGODB_URI_HOTEL2 || 'mongodb+srv://user:pass@cluster.mongodb.net/Hotel2',
    // Yeni oteller ekledikçe buraya ekleyebilirsiniz
  };
  
  return connections[hotelId] || process.env.MONGODB_URI_DEFAULT;
};

// Email yapılandırması (her otel için farklı olabilir)
const getEmailConfig = (hotelId) => {
  const emailConfigs = {
    'hotel1': {
      host: process.env.EMAIL_HOST || 'smtp.gmail.com',
      port: parseInt(process.env.EMAIL_PORT) || 465,
      secure: process.env.EMAIL_SECURE === 'true',
      auth: {
        user: process.env.EMAIL_USER_HOTEL1 || 'default@gmail.com',
        pass: process.env.EMAIL_PASS_HOTEL1 || 'password'
      }
    },
    'hotel2': {
      // Otel 2 için farklı email yapılandırması
      host: process.env.EMAIL_HOST || 'smtp.gmail.com',
      port: parseInt(process.env.EMAIL_PORT) || 465,
      secure: process.env.EMAIL_SECURE === 'true',
      auth: {
        user: process.env.EMAIL_USER_HOTEL2 || 'default@gmail.com',
        pass: process.env.EMAIL_PASS_HOTEL2 || 'password'
      }
    }
  };
  
  return emailConfigs[hotelId] || emailConfigs['hotel1']; // Varsayılan yapılandırma
};

// Otel-spesifik diğer yapılandırmalar için buraya ekleyebilirsiniz

module.exports = {
  getMongoDBConnectionString,
  getEmailConfig,
  port: process.env.PORT || 8080
}; 