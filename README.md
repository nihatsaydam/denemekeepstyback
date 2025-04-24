# Keepsty Otel Yönetim Sistemi

Bu proje, birden fazla otel için tek bir kod tabanı üzerinden hizmet verebilen, ölçeklenebilir bir otel yönetim sistemi backend'idir. Google Cloud Platform üzerinde çalışacak şekilde tasarlanmıştır.

## Özellikler

- **Çoklu Kiracılık (Multi-tenancy)**: Aynı kod tabanı birden fazla otele hizmet verebilir
- **İzolasyon**: Her otelin verileri ayrı MongoDB veritabanlarında saklanır
- **CI/CD**: GitHub ile entegre, otomatik deploy pipeline'ı
- **Ölçeklenebilirlik**: Google Cloud App Engine kullanarak kolayca ölçeklenebilir
- **Modüler Yapı**: Yeni modüller ve servisler eklemek çok kolay

## Kurulum ve Çalıştırma

### Yerel Geliştirme Ortamı

1. Repository'yi klonlayın:
```bash
git clone https://github.com/username/keepsty-backend.git
cd keepsty-backend
```

2. Bağımlılıkları yükleyin:
```bash
npm install
```

3. `.env` dosyasını oluşturun (`.env.example` dosyasını referans alabilirsiniz):
```bash
cp .env.example .env
# .env dosyasını düzenleyin ve gerekli değerleri ekleyin
```

4. Servisi başlatın:
```bash
npm start
```

### Google Cloud'a Deploy Etme

1. Google Cloud SDK'yı kurun
2. Projeyi seçin:
```bash
gcloud config set project your-project-id
```

3. Uygulamayı deploy edin:
```bash
gcloud app deploy
```

Alternatif olarak, GitHub ile entegre Cloud Build kullanarak otomatik deployment da yapabilirsiniz.

## Çoklu Otel Yapılandırması

Her otel için aşağıdaki ayarları yapın:

1. MongoDB bağlantısı oluşturun
2. İlgili otel için gerekli ortam değişkenlerini ayarlayın
3. DNS yapılandırması (subdomain tabanlı ayrım için)

## API Endpointleri

Sistem şu ana hizmetleri içerir:

- Housekeeping / Oda Temizlik Hizmeti
- Room Service / Oda Servisi
- Concierge / Danışma Hizmeti
- Laundry / Çamaşırhane Hizmeti
- Tech Support / Teknik Destek
- Bellboy / Taşıyıcı Hizmeti
- Ask / Soru-Cevap Hizmeti

## Mimarinin Mantığı

Sistem, request-time tenant resolution stratejisi kullanır:

1. Her istekte otel kimliği belirlenir (subdomain, query param, header)
2. Bu kimlik kullanılarak doğru veritabanı bağlantısı seçilir
3. Modeller bu bağlantı üzerinden dinamik olarak oluşturulur
4. İşlemler izole edilmiş veritabanı üzerinde gerçekleştirilir

## Güvenlik

- Hassas bilgiler (MongoDB bağlantı stringleri, e-posta şifreleri vb.) ortam değişkenlerinde tutulur ve GitHub'a commit edilmez
- Her otel kendi veritabanına erişim sağlar, çapraz erişim engellenir

## Destek

Sorunlar ve öneriler için issue açabilir veya pull request gönderebilirsiniz.

## Lisans

Bu proje özel lisanslıdır. Tüm hakları saklıdır. 