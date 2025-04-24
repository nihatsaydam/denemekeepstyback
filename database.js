const mongoose = require('mongoose');
const config = require('./config');

// Bağlantı havuzu - farklı veritabanlarına birden fazla bağlantı yönetimi
const connections = {};

/**
 * Belirli bir otel kimliği için MongoDB bağlantısı oluşturur veya mevcut ise döndürür
 * @param {string} hotelId - Otel kimliği
 * @returns Mongoose bağlantısı
 */
const getConnection = async (hotelId) => {
  // Bağlantı zaten varsa, yenisini oluşturmadan dön
  if (connections[hotelId]) {
    return connections[hotelId];
  }

  // Otel ID'sine göre bağlantı stringini al
  const connectionString = config.getMongoDBConnectionString(hotelId);
  
  if (!connectionString) {
    throw new Error(`MongoDB connection string for hotel ${hotelId} not found`);
  }

  try {
    // Yeni bağlantı oluştur
    const connection = await mongoose.createConnection(connectionString, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });

    // Bağlantıyı cache'le
    connections[hotelId] = connection;
    console.log(`Connected to MongoDB for hotel: ${hotelId}`);
    
    return connection;
  } catch (error) {
    console.error(`Error connecting to MongoDB for hotel ${hotelId}:`, error);
    throw error;
  }
};

/**
 * Belirli bir otel için model oluştur
 * @param {string} modelName - Model adı
 * @param {mongoose.Schema} schema - Mongoose şeması
 * @param {string} collectionName - Koleksiyon adı (opsiyonel)
 * @param {string} hotelId - Otel kimliği
 * @returns Mongoose model
 */
const createModel = async (modelName, schema, collectionName, hotelId) => {
  const connection = await getConnection(hotelId);
  return connection.model(modelName, schema, collectionName);
};

/**
 * Tüm bağlantıları kapat
 */
const closeAllConnections = async () => {
  const closePromises = Object.values(connections).map(conn => conn.close());
  await Promise.all(closePromises);
  connections = {};
  console.log('All MongoDB connections closed');
};

module.exports = {
  getConnection,
  createModel,
  closeAllConnections
}; 