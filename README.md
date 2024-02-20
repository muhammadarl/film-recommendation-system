# Laporan Proyek Machine Learning - Muhammad Syiarul Amrullah

## Project Overview

Penelitian ini bertujuan untuk mengembangkan sistem rekomendasi yang dipersonalisasi untuk perusahaan distributor film. Perusahaan distributor film memiliki tugas penting dalam menghadirkan film-film terbaru dan berkualitas kepada penonton. Dalam industri ini, keberhasilan sebuah film dalam mencapai kesuksesan tidak hanya ditentukan oleh kualitas film itu sendiri, tetapi juga oleh sejauh mana film tersebut dapat dijangkau oleh penonton potensial. Oleh karena itu, sistem rekomendasi yang dipersonalisasi sangat penting untuk membantu perusahaan distributor film menghadirkan film-film yang tepat kepada penonton yang tepat. berdasarkan penelitian, recommendation system dapat meningkatkan minat atau penjualan suatu produk [[1](https://www.semanticscholar.org/paper/K-Nearest-Neighbors-Method-for-Recommendation-in-Anamisa-Jauhari/c3f89e63f48d76a32407bd99438dadc78015360f)]. Maka dari itu, recommendation system ditujukan untuk meningkatkan minat penonton terhadap film dengan karakteristik serupa dan rating tinggi.

penelitian ini menggunakan teknik content-based filtering dan collaborative filtering. analisa preferensi pengguna berdasarkan film-film yang telah mereka tonton, sistem ini akan merekomendasikan film-film lain yang memiliki karakteristik serupa yang mungkin belum pernah mereka tonton. Tujuan utama proyek ini adalah untuk meningkatkan pengalaman pengguna dalam memilih film yang ingin ditonton serta meningkatkan penjualan perusahaan dengan merekomendasikan film yang belum pernah ditonton oleh pengguna. Dengan memberikan rekomendasi yang relevan, diharapkan penonton akan lebih tertarik untuk menonton film-film baru yang dihadirkan oleh perusahaan distributor film, sehingga meningkatkan penjualan dan keuntungan perusahaan.

## Business Understanding

Penelitian ini difokuskan pada dua permasalahan utama yang dihadapi oleh perusahaan distributor film. Pertama, bagaimana membuat sistem rekomendasi yang dipersonalisasi dengan teknik content-based filtering? Dalam industri film yang kompetitif, perusahaan distributor film perlu memastikan bahwa mereka dapat menyajikan film-film yang paling sesuai dengan preferensi penonton mereka. Dengan menggunakan teknik content-based filtering, perusahaan dapat menganalisis preferensi penonton berdasarkan film-film yang telah mereka tonton sebelumnya dan merekomendasikan film-film lain yang memiliki kesamaan karakteristik.

Kedua, bagaimana perusahaan distributor film dapat merekomendasikan film lain yang mungkin disukai dan belum pernah ditonton oleh pengguna? Seiring dengan perkembangan teknologi dan platform streaming, penonton memiliki akses yang lebih besar terhadap berbagai pilihan film. Namun, ini juga membuatnya lebih sulit bagi perusahaan distributor film untuk menjangkau penonton potensial yang belum pernah menonton film-film tertentu. Dengan menggunakan sistem rekomendasi yang dipersonalisasi, perusahaan dapat merekomendasikan film-film yang belum pernah ditonton oleh pengguna namun memiliki potensi besar untuk disukai.

Penerapan sistem rekomendasi yang dipersonalisasi dalam industri film dapat memiliki dampak yang signifikan pada peningkatan penjualan dan keuntungan perusahaan distributor film. Pertama, dengan menyajikan film-film yang lebih sesuai dengan preferensi pengguna, sistem rekomendasi dapat meningkatkan kemungkinan pengguna untuk menonton film-film baru yang direkomendasikan. Hal ini dapat menghasilkan peningkatan dalam penjualan tiket bioskop, penjualan DVD atau Blu-ray, atau penonton yang menonton film secara digital.

Kedua, sistem rekomendasi dapat membantu dalam meningkatkan keterlibatan pengguna dan retensi pelanggan. Dengan menyajikan rekomendasi yang relevan dan menarik, sistem dapat meningkatkan pengalaman pengguna, membuat mereka lebih cenderung untuk kembali menggunakan layanan perusahaan distributor film. Hal ini dapat mengurangi churn rate, yaitu jumlah pelanggan yang berhenti menggunakan layanan, dan meningkatkan loyalitas pelanggan.

Selain itu, dengan mendorong penonton untuk menonton film-film baru yang direkomendasikan, sistem rekomendasi dapat membantu perusahaan distributor film dalam memperkenalkan dan mempromosikan konten baru. Hal ini dapat membantu dalam meningkatkan popularitas film-film tersebut dan meningkatkan pendapatan perusahaan dari penjualan tiket, lisensi, dan produk-produk terkait film.

Secara keseluruhan, sistem rekomendasi yang dipersonalisasi dapat menjadi alat yang sangat efektif dalam meningkatkan kinerja dan keberhasilan perusahaan distributor film dengan meningkatkan penjualan, mengurangi churn rate, dan meningkatkan pengalaman pengguna.

### Problem Statements

Rumusan masalah pada penelitian ini sebagai berikut:
- Bagaimana membuat sistem rekomendasi yang berdasarkan film yang sedang dilihat?
- Bagaimana perusahaan distributor film dapat merekomendasikan film lain yang mungkin disukai dan belum pernah ditonton oleh pengguna?
- Bagaimana development content-based filtering model dengan ketepatan tinggi?
- Bagaimana development collaborative filtering model dengan score tinggi?

### Goals

Tujuan pada penelitian ini sebagai berikut:
- Menghasilkan sejumlah rekomendasi berdasarkan film yang sedang dilihat pengguna.
- Menghasilkan sejumlah rekomendasi film yang sesuai dengan preferensi pengguna dan belum pernah ditonton sebelumnya.
- Memiliki hasil Precision pada content-based filtering melebihi 90%.
- Memiliki hasil RMSE(Root Mean Square Error) pada validation kurang dari 0.25


### Solution statements
- Penggunaan Content-based Filtering untuk menghasilkan rekomendasi berdasarkan film yang sedang dilihat pengguna
- Penggunaan Collaborative Filtering untuk menghasilkan rekomendasi film sesuai dengan preferensi pengguna dan belum ditonton sebelumnya.

## Data Understanding
Dataset yang digunakan untuk proyek ini diperoleh dari situs kaggle yang dapat diunduh melalui [Kaggle](https://www.kaggle.com/datasets/nicoletacilibiu/movies-and-ratings-for-recommendation-system). berikut detail dari dataset yang digunakan:
1. Movies Dataset
Movies dataset merupakan dataset yang berisi judul film dan genre. berikut struktur dari movies dataset

    | Feature  | type | Row |
    | ------------- | ------------- |------------- |
    | movieId  | int  | 9742  |
    | title  | object  | 9742  |
     | genres  | object  | 9742  |
   
     Tabel 1. Summary Movies Dataset
     
3. Ratings
Ratings dataset merupakan dataset yang berisi user, ratings dan movieId. berikut struktur dari Ratings dataset
    | Feature  | type | Row |
    | ------------- | ------------- |------------- |
    | movieId  | int  | 100836  |
    | userId  | int  | 100836  |
     | rating  | float  | 100836  |
     | timestamp  | int  | 100836  |
   
    Tabel 2. Summary Ratings Dataset
### Exploratory Data Analysis

#### Univariate Analysis
**Ratings**
![Distribution ratings data](https://github.com/muhammadarl/film-recommendation-system/blob/main/img/distribution%20rating.png?raw=true)

Gambar 1. Distribution ratings data

Berdasarkan gambar 1, dapat dilihat bahwa nilai rating berkisar antara 0.5 hingga 4.5. Nilai rating maksimum yang diberikan oleh pengguna adalah 4.5, sedangkan nilai rating minimum adalah 0.5. Secara khusus, terdapat sekitar 25.000 data yang memiliki rating 4.0, menjadikannya rating yang paling banyak diberikan oleh pengguna. Di sisi lain, rating 1.0, 1.5, dan 0.5 memiliki jumlah data yang jauh lebih sedikit, masing-masing tidak melebihi 5.000 data. Hal ini menunjukkan bahwa pengguna cenderung memberikan rating yang lebih tinggi daripada rating yang lebih rendah, dengan rating 4.0 menjadi pilihan yang paling umum.

**Genres**
![Distribution genres data](https://github.com/muhammadarl/film-recommendation-system/blob/main/img/distribution%20genre.png?raw=true)

Gambar 2. Distribution genres data
Berdasarkan gambar 2, dapat dilihat bahwa genre "Drama" memiliki jumlah data yang paling banyak dibandingkan dengan genre lainnya. Di sisi lain, genre "Film-Noir" dan "Genres Lainnya" memiliki jumlah data yang relatif sedikit. Oleh karena itu, dari segi jumlah data, genre "Drama" menjadi genre yang paling banyak muncul dalam dataset ini.

**Years**
![Distribution years data](https://github.com/muhammadarl/film-recommendation-system/blob/main/img/distribution%20year.png?raw=true)

Gambar 3. Distribution Years data
Berdasarkan gambar 3, terlihat bahwa tahun 2002 memiliki jumlah data yang paling banyak dibandingkan dengan tahun lainnya. Di sisi lain, tahun 1996 dan tahun-tahun lainnya memiliki jumlah data yang relatif sedikit. Oleh karena itu, dari segi jumlah data, tahun 2002 menjadi tahun dengan publikasi film paling banyak dalam dataset ini.

#### Multivariate Analysis
**Ratings and Genres**
![Count of ratings 5.0 by genre](https://github.com/muhammadarl/film-recommendation-system/blob/main/img/Count%20of%20rating%20by%20Genre%205.0%20rating.png?raw=true)

Gambar 4. Count of ratings 5.0 by genre

Berdasarkan gambar 4, terlihat bahwa genre "Drama" memiliki jumlah rating tinggi paling banyak dibandingkan dengan genre lainnya. Hal ini menunjukkan bahwa film-film dengan genre "Drama" cenderung mendapatkan respons positif dari penonton dalam bentuk rating yang tinggi. Selain itu, genre "Adventure" memiliki jumlah rating tinggi yang signifikan, terutama jika dijumlahkan dengan jumlah rating tinggi dari lima genre teratas lainnya.

Dari data ini, dapat disimpulkan bahwa penonton cenderung lebih tertarik dengan film-film bergenre "Drama" karena jumlah rating tinggi yang diberikan. Meskipun genre "Adventure" juga memiliki jumlah rating tinggi yang cukup signifikan, genre "Drama" tetap menjadi pilihan utama penonton berdasarkan jumlah rating tinggi yang paling banyak. Hal ini menunjukkan bahwa film-film dengan genre "Drama" memiliki daya tarik yang kuat bagi penonton dan dapat dianggap sebagai genre yang populer dan diminati oleh penonton.

![Count of ratings 0.5 by genre](https://github.com/muhammadarl/film-recommendation-system/blob/main/img/Count%20of%20rating%20by%20Genre%200.5%20rating.png?raw=true)

Gambar 5. Count of ratings 0.5 by genre

Berdasarkan gambar 5, terlihat bahwa genre "Comedy" memiliki jumlah rating rendah paling banyak dibandingkan dengan genre lainnya. Hal ini menunjukkan bahwa film-film dengan genre "Comedy" cenderung mendapatkan respons yang kurang positif dari penonton dalam bentuk rating yang rendah. Selain itu, genre "Adventure" juga memiliki jumlah rating rendah yang signifikan, terutama jika dijumlahkan dengan jumlah rating rendah dari lima genre teratas lainnya.

Dari data ini, dapat disimpulkan bahwa penonton cenderung kurang tertarik dengan film-film bergenre "Comedy" karena jumlah rating rendah yang diberikan. Meskipun genre "Adventure" juga memiliki jumlah rating rendah yang cukup signifikan, genre "Comedy" tetap menjadi salah satu genre yang paling kurang diminati oleh penonton berdasarkan jumlah rating rendah yang paling banyak. Hal ini menunjukkan bahwa film-film dengan genre "Comedy" mungkin memiliki daya tarik yang lebih rendah bagi penonton dan dapat dianggap sebagai genre yang kurang populer atau diminati dibandingkan dengan genre lainnya.

**Ratings and Years**
![Count of ratings 5.0 by year](https://github.com/muhammadarl/film-recommendation-system/blob/main/img/Count%20of%20rating%20by%20Year5.0%20rating.png?raw=true)

Gambar 6. Count of ratings 5.0 by year

Berdasarkan gambar 6. Tahun 1994 memiliki ratings tinggi paling banyak dan adventure memiliki ratings tinggi dengan jumlah dari top 5 lainnya. Maka dari itu, penonton lebih tertarik dengan film dengan genre drama.

![Count of ratings 0.5 by year](https://github.com/muhammadarl/film-recommendation-system/blob/main/img/Count%20of%20rating%20by%20year%200.5%20rating.png?raw=true)

Gambar 7. Count of ratings 0.5 by year

Berdasarkan gambar 7. Tahun 2001 memiliki ratings rendah paling banyak dan tahun 2003 memiliki ratings rendah dengan jumlah dari top 5 lainnya. Maka dari itu, penonton tidak tertarik dengan film pada tahun 2001..

## Data Preparation
setelah data understanding, selanjutnya data preparation. Pada bagian ini dilakukan beberapa penerapan untuk mempersiapkan data. beberapa tahap seperti merge data dan change data type. berikut penerapannya:

1. Merge Data
Tahap Pertama yang dilakukan yaitu merge data. Merge data antara movie dan rating perlu dilakukan dalam analisis data untuk menggabungkan informasi dari kedua dataset tersebut. Data movie menyediakan informasi tentang film-film seperti judul, genre, dan tahun rilis, sementara data rating berisi informasi tentang rating yang diberikan oleh pengguna untuk setiap film. Dengan menggabungkan kedua data ini, analisa bagaimana rating film berkorelasi dengan atribut-atribut film tersebut, seperti genre atau tahun rilis. Selain itu, merge data memungkinkan analisis peringkat film berdasarkan rating yang diberikan oleh pengguna, sehingga dapat memberikan wawasan tentang preferensi pengguna terhadap jenis film tertentu. Merge data juga penting untuk membangun sistem rekomendasi yang lebih baik dengan memperhitungkan preferensi pengguna yang dinyatakan melalui rating yang diberikan. Dengan demikian, merge data antara movie dan rating memungkinkan analisis yang lebih komprehensif tentang preferensi pengguna, peringkat film, dan tren dalam industri film.
2. Missing Value

    ![Missing Value](https://github.com/muhammadarl/film-recommendation-system/blob/main/img/missing_value.png?raw=true)
    
    Gambar 8. Missing Value
    
    Berdasarkan gambar 8. tidak terdapat missing value dari keseluruhan data, maka dari itu dataset siap digunakan untuk development recommendation system.
3. Change Data Type
Setelah tahap merge data, selanjutnya tahap change data type. ada 1 feature yang memiliki tipe data ordinal yaitu rating.Perubahan tipe data dari "object" ke "category" adalah proses yang melibatkan konversi nilai-nilai kategori dalam kolom menjadi nilai numerik yang mewakili tingkat ordinal. Perubahan tipe data dari object ke category perlu dilakukan untuk mengoptimalkan penggunaan memori dan meningkatkan performa analisis data. Tipe data category lebih efisien dalam penggunaan memori karena menggunakan pendekatan pengkodean kategori yang menggantikan nilai unik dengan bilangan bulat yang lebih kecil daripada representasi string atau objek. Selain itu, penggunaan tipe data category juga dapat meningkatkan performa operasi pada kolom tersebut, seperti pengurutan atau pengelompokan data, karena data yang direpresentasikan dalam bentuk kategori lebih mudah untuk diurutkan dan dikelompokkan. Selain efisiensi memori dan performa, menggunakan tipe data category juga mempermudah analisis data yang melibatkan kategori dengan memanfaatkan fitur-fitur khusus untuk kategori, seperti menetapkan urutan kategori atau memberi label kategori secara eksplisit. Namun, perlu diingat bahwa penggunaan tipe data category juga dapat menambah kompleksitas kode, terutama dalam pengkodean ulang kembali ke nilai asli jika diperlukan. Oleh karena itu, pemilihan tipe data haruslah dilakukan dengan seimbang antara efisiensi memori, performa analisis, dan kompleksitas kode yang dihasilkan.

## Modeling
Setelah tahap Data Preparation, selanjutnya tahap modelling. Modelling memiliki 2 tahap yaitu collaborative filtering dan content based filtering. Content-Based Filtering adalah teknik dalam sistem rekomendasi yang menggunakan karakteristik atau konten dari item untuk merekomendasikan item yang serupa kepada pengguna. Collaborative Filtering adalah teknik dalam sistem rekomendasi yang menggunakan informasi dari sejumlah besar pengguna dan interaksi mereka dengan item untuk membuat rekomendasi. berikut merupakan penerapan algoritma recommendation:
### Content-based filtering
Dalam konteks sistem rekomendasi film, misalnya, content-based filtering akan menganalisis atribut-atribut film seperti genre untuk merekomendasikan film yang memiliki karakteristik serupa dengan film yang disukai pengguna. Kelebihan dari content-based filtering termasuk kemampuannya untuk memberikan rekomendasi yang personalisasi sesuai dengan preferensi pengguna, tidak memerlukan data eksternal seperti peringkat pengguna lainnya, dan dapat menangani item baru dengan baik. Namun, metode ini juga memiliki kelemahan, seperti cenderung memberikan rekomendasi yang terlalu mirip dengan item yang sudah disukai pengguna, kesulitan dalam memberikan rekomendasi untuk pengguna atau item baru, dan keterbatasan dalam menangkap preferensi pengguna yang kompleks. Oleh karena itu, dalam praktiknya, kombinasi dari beberapa metode rekomendasi sering digunakan untuk memberikan rekomendasi yang lebih baik secara keseluruhan. Penerapan algoritma ini memiliki beberapa tahapan yaitu vektorisasi dan _cosine similiarity_. Berikut penerapan tahapannya:
1. Vektorisasi
tahap pertama dari modelling yaitu vektorisasi. Vektorisasi adalah proses mengubah teks menjadi representasi vektor numerik. Dalam NLP, kata-kata atau token dalam teks diubah menjadi vektor numerik, yang dapat digunakan oleh algoritma machine learning untuk mempelajari pola, membuat prediksi, atau melakukan tugas lainnya. Teknik yang digunakan untuk vektorisasi adalah Tf-IDf. Term Frequency-Inverse Document Frequency (TF-IDF) adalah metode vektorisasi teks yang digunakan untuk mengukur seberapa penting suatu kata dalam sebuah dokumen dalam konteks seluruh koleksi dokumen. TF-IDF menghitung dua nilai untuk setiap kata dalam dokumen: frekuensi kemunculan kata tersebut (TF) dan kebalikannya dari frekuensi kemunculan kata tersebut di seluruh dokumen (IDF).

    Kelebihan dari TF-IDF adalah kemampuannya untuk memberikan bobot yang lebih tinggi pada kata-kata yang jarang muncul tetapi muncul dalam dokumen tertentu (tinggi TF dan rendah IDF), sehingga membantu mengidentifikasi kata-kata yang unik atau spesifik untuk dokumen tersebut. TF-IDF juga dapat membantu mengatasi masalah kata-kata umum yang sering muncul di banyak dokumen tetapi tidak memberikan informasi yang signifikan (seperti "the" atau "and").
    
    Namun, TF-IDF juga memiliki beberapa kekurangan. Pertama, TF-IDF tidak memperhitungkan urutan kata atau struktur kalimat, sehingga tidak cocok untuk tugas-tugas NLP yang memerlukan pemahaman sintaksis atau semantik yang kompleks. Selain itu, penggunaan TF-IDF dapat menjadi rumit jika dokumen memiliki panjang yang bervariasi atau jika koleksi dokumen sangat besar, karena perhitungan IDF dapat menjadi tidak efisien. berikut adalah formula dari TF-IDF:
![tf-idf Formula](https://miro.medium.com/v2/resize:fit:1358/1*V9ac4hLVyms79jl65Ym_Bw.jpeg)
Gambar 9. tf-idf Formula
2. Cosine Similiarity
Cosine similarity adalah metrik yang digunakan untuk mengukur seberapa mirip dua vektor non-nol dalam ruang berdimensi banyak. Cosine similarity memiliki beberapa kelebihan yang membuatnya menjadi metode yang populer dalam analisis data. Pertama, cosine similarity mudah diinterpretasikan, karena hasilnya berkisar antara -1 hingga 1, di mana nilai yang lebih tinggi menunjukkan kedua vektor yang lebih mirip. Selain itu, cosine similarity tidak dipengaruhi oleh magnitudo dari vektor, hanya arahnya yang penting, sehingga cocok untuk data di mana magnitudo tidak relevan. Metode ini juga efisien secara komputasi, terutama untuk data dengan dimensi yang tinggi, dan bekerja dengan baik untuk data yang memiliki banyak nilai nol (sparse), seperti data teks. Namun, cosine similarity juga memiliki beberapa kekurangan. Pertama, metode ini tidak sensitif terhadap perbedaan bobot antar fitur, sehingga tidak cocok jika bobot-fitur tersebut penting dalam perbandingan. Selain itu, cosine similarity mengasumsikan hubungan linier antara fitur, sehingga tidak cocok untuk data yang memiliki hubungan non-linear. Metode ini juga tidak memperhitungkan hubungan antar fitur dalam vektor, hanya memperhatikan arah vektor, dan sensitif terhadap perbedaan panjang vektor, yang dapat menghasilkan hasil yang tidak akurat jika panjang vektor sangat berbeda. Meskipun memiliki kekurangan, cosine similarity tetap menjadi pilihan yang populer dalam banyak aplikasi karena kesederhanaannya dan kemampuannya untuk mengatasi masalah sparsity dalam data.Dalam konteks sistem rekomendasi, cosine similarity sering digunakan untuk membandingkan kesamaan antara dua item atau dua pengguna berdasarkan preferensi mereka terhadap item. Untuk menghitung cosine similarity antara dua vektor, berikut adalah rumus cosine similarity:
![Cosine Similarity Formula](https://miro.medium.com/v2/resize:fit:1400/1*LfW66-WsYkFqWc4XYJbEJg.png)
Gambar 10. Cosine Similarity Formula
Setelah mendapatkan cosine similarity, berikut adalah sample data hasil cosine similarity.
    | Title  | Stage Beauty (2004) | The Expendables 3 (2014)  |Love at First Bite (1979)	|
    | -------- | ---- |----- |------|
    | Ali G Indahouse (2002)  | 0.000000	  |0.000000	|0.410816|
    | Major League: Back to the Minors (1998)   | 0.000000	  |0.000000	|0.410816|
   
    Tabel 3. Sample Data hasil COsine Similarity

Model content based filtering dicoba menggunakan preferensi movie sebagai berikut:
| Title  | genres |
| -------| ------ |
| Old Boy (2003)|Mystery, Thriller|

Tabel 4. Sample Data sebagai percobaan content-based filtering
Hasilnya, rekomendasi yang dihasilkan sebagai berikut:

| Title  | genres |
| -------| ------ |
|The Wailing (2016)|Mystery, Thriller|
|Memento (2000)|Mystery, Thriller|
|Body Double (1984)|Mystery, Thriller|
|Saboteur (1942)|Mystery, Thriller|
|Pacific Heights (1990)|Mystery, Thriller|

Tabel 5. Hasil Content-based filtering

### Collaborative Filtering
Terdapat dua jenis collaborative filtering: user-based dan item-based. User-Based Collaborative Filtering mengidentifikasi pengguna yang memiliki preferensi serupa dengan pengguna tertentu dan merekomendasikan item yang disukai oleh pengguna serupa tersebut. Sementara itu, Item-Based Collaborative Filtering mencari item yang memiliki kesamaan dalam preferensi pengguna, misalnya item yang sering disukai oleh pengguna yang sama. Kelebihan dari collaborative filtering termasuk efektif untuk item atau pengguna baru karena dapat memanfaatkan informasi dari pengguna yang sudah ada, dan mampu mengatasi masalah over-specialization dengan memberikan rekomendasi yang lebih beragam. Namun, metode ini juga memiliki kelemahan, seperti kesulitan dalam menangani cold start untuk item atau pengguna baru yang belum memiliki data interaksi yang cukup, serta masalah sparsity dan skala yang timbul ketika jumlah pengguna dan item sangat besar. Kombinasi dengan metode lain seperti content-based filtering sering digunakan untuk meningkatkan kualitas rekomendasi secara keseluruhan. Penelitian ini menggunakan pendekatan Deep learning. Pendekatan collaborative filtering dengan deep learning menggabungkan konsep-konsep dari collaborative filtering (CF) dan deep learning untuk meningkatkan kualitas rekomendasi dalam sistem rekomendasi. CF adalah metode yang menggunakan informasi dari pengguna lain untuk membuat rekomendasi, sedangkan deep learning adalah teknik pembelajaran mesin yang menggunakan jaringan saraf tiruan untuk memahami dan mempelajari representasi data yang kompleks.

Dalam konteks rekomendasi, deep learning dapat digunakan untuk memodelkan hubungan yang kompleks antara pengguna, item, dan interaksi mereka. Misalnya, deep learning dapat digunakan untuk mempelajari representasi vektor dari pengguna dan item yang lebih kaya dan informatif, daripada representasi yang dihasilkan secara manual. Hal ini memungkinkan model untuk menangkap pola yang lebih halus dan kompleks dalam data rekomendasi.

Keuntungan pendekatan collaborative filtering dengan deep learning adalah kemampuannya untuk mengatasi beberapa masalah yang dihadapi oleh metode CF tradisional, seperti cold start (ketika ada item baru atau pengguna baru) dan sparsity (ketika hanya sedikit informasi interaksi yang tersedia). Deep learning juga dapat meningkatkan kualitas rekomendasi dengan memanfaatkan informasi yang lebih kaya dari data rekomendasi.

Namun, pendekatan ini juga memiliki beberapa kekurangan. Penggunaan deep learning memerlukan jumlah data yang besar untuk melatih model dengan baik, dan memerlukan komputasi yang lebih intensif dibandingkan dengan metode tradisional. Selain itu, interpretasi model deep learning juga lebih sulit dibandingkan dengan model tradisional, sehingga sulit untuk menjelaskan mengapa model memberikan rekomendasi tertentu kepada pengguna. berikut merupakan hasil rekomendasi collaborative filtering:
|preferensi user yang digunakan|
|--------------------------------|
|userId : 286|

Tabel 6. Preferensi User Collaborative Filtering

|movie with high ratings from user 286|
|--------------------------------|
|GoldenEye (1995) : Action, Adventure, Thriller|
|Rob Roy (1995) : Action, Drama, Romance, War|
|Something to Talk About (1995) : Comedy, Drama, Romance|
|Walk in the Clouds, A (1995) : Drama, Romance|
|I.Q. (1994) : Comedy, Romance|

Tabel 7. Hasil Collaborative Filtering(Movie with high ratings)

|Top 10 movie recommendation 286|
|--------------------------------|
|Streetcar Named Desire, A (1951) : Drama|
|Lawrence of Arabia (1962) : Adventure, Drama, War|
|Touch of Evil (1958) : Crime, Film-Noir, Thriller|
|Autumn Sonata (Höstsonaten) (1978) : Drama|
|Lifeboat (1944) : Drama, War|
|Guess Who's Coming to Dinner (1967) : Drama|
|Trial, The (Procès, Le) (1962) : Drama|
|Captain Fantastic (2016) : Drama|
|Band of Brothers (2001) : Action, Drama, War|
|Three Billboards Outside Ebbing, Missouri (2017) : Crime, Drama|

Tabel 8. Hasil Collaborative Filtering(Movie recommendation)

## Evaluation
setelah modelling dilakukan, selanjutnya adalah evaluation model. pada tahap ini dilakukan evaluasi pada kinerja model menggunakan Precision (Content based filtering) dan RMSE (Collaborative Filtering). berikut evaluation untuk content-based filtering dan collaborative filtering:
1. Content Based Filtering
Pada evaluasi content-based filtering menggunakan precision. Precision dalam sistem rekomendasi mengacu pada seberapa akurat sistem tersebut dalam merekomendasikan item yang sesuai dengan preferensi atau minat pengguna. Precision dihitung sebagai rasio antara jumlah item yang relevan yang direkomendasikan oleh sistem dengan jumlah total item yang direkomendasikan. Precision penting dalam sistem rekomendasi karena mengukur seberapa baik sistem dalam memilih item yang benar-benar diminati oleh pengguna. Sebuah sistem yang memiliki precision tinggi akan memberikan rekomendasi yang lebih relevan dan berguna bagi pengguna, sehingga meningkatkan kepuasan pengguna dan efektivitas sistem secara keseluruhan. berikut formula precision pada recommendation system:
![Precision Formula](https://i.stack.imgur.com/W8rc6.png)
Gambar 4. Precision Formula
Hasil dari evaluasi yang telah dilakukan memiliki hasil sebagai berikut:
$$Precision = {relevantrecommendation \over total recommendation}*100$$

    $$Precision = {5 \over 5}*100$$%
    $$Precision = 100$$%
    Berdasarkan  hasil diatas, relevant recommendation values diambil dari genre, jika genre sama dengan preferensi movie, maka dianggap relevant. Hasilnya, terdapat 5 movie genre yang sama dengan preferensi movienya dan total recommendation 5, maka dari itu precision score 100%.
2. Collaborative Filtering
pada evaluasi collaborative filtering menggunakan RMSE. berikut penjelasan dari metriks RMSE:
Root Mean Square Error (RMSE) adalah metrik evaluasi yang umum digunakan untuk mengukur seberapa baik suatu model regresi dapat memprediksi nilai yang sebenarnya. RMSE mengukur seberapa jauh rata-rata prediksi model dari nilai yang diamati. Secara matematis, RMSE didefinisikan sebagai akar kuadrat dari rata-rata dari kuadrat selisih antara nilai prediksi dan nilai aktual. berikut adalah formula RMSE:
![RMSE Formula](https://media.geeksforgeeks.org/wp-content/uploads/20200622171741/RMSE1.jpg)
Gambar 4. RMSE Formula
Berikut hasil RMSE dari model collaborative filtering:
![evaluation RMSE](https://github.com/muhammadarl/film-recommendation-system/blob/main/img/evaluation_rmse.png?raw=true)
Gambar 11. evaluation RMSE

    Berdasarkan gambar 11, menunjukan RMSE pada data test berada dibawah 0.2 sedangkan trainingnya sekitar 0.25. RMSE Score yang dekat dengan 16% masih dapat dianggap baik [[2](https://www.semanticscholar.org/paper/Hydrodynamic-and-Sediment-Transport-Simulation-at-Wahyudi-Suntoyo/bf3bab0b16e8aff150bb01068e6c0869b1a229b3)]. Jarak training score dan test score tidak terlalu jauh sehingga diindikasikan model tidak overfitting [[3](https://www.semanticscholar.org/paper/An-Overview-of-Overfitting-and-its-Solutions-Ying/75d50a601d4830fae3a24ff55f2795ef3911924e)]. Overfitting pada sistem rekomendasi dapat terjadi karena keterbatasan data, fitur-fitur yang terlalu kompleks, atau model yang terlalu besar. Kurangnya regularisasi dan penggunaan metrik evaluasi yang tidak tepat juga dapat menyebabkan overfitting. Untuk mengatasi masalah ini, penting untuk menggunakan teknik-teknik seperti validasi silang, regularisasi, dan pemantauan kinerja model dengan cermat.
## Conclussion
Hasil yang telah dipaparkan menunjukan bahwa content-based filtering memiliki akurasi yang unggul dari collaborative filtering dengan precision 100%, precision score pada recommendation system menunjukan bahwa hasil yang diberikan recommendation system relevant dengan prefensi film yang ditentukan. hal tersebut berhasil menjawab problem statement penelitian ini seperti, Bagaimana membuat sistem rekomendasi yang berdasarkan film yang sedang dilihat? jawabannya menggunakan content-based filtering metode cosine similarity dan Bagaimana perusahaan distributor film dapat merekomendasikan film lain yang mungkin disukai dan belum pernah ditonton oleh pengguna? jawabannya menggunakan collaborative filtering metode deep learning untuk menghasilkan rekomendasi berdasarkan film yang telah diberi rating dan karakteristik filmnya. Bagaimana development content-based filtering model dengan ketepatan tinggi? menggunakan metode cosine similarity dan genres sebagai preferensi. Hasilnya precision 100% menunjukan bahwa model memberikan rekomendasi yang tepat. Bagaimana development collaborative filtering model dengan score tinggi? menggunakan metode deep learning dan metriks RMSE sebagai penilaian. Hasilnya, training RMSE 0.18 dan Test(validation) RMSE 0.25 perbedaan yang tidak terlalu jauh menunjukan bahwa model tidak overfitting dan RMSE score termasuk unggul.
