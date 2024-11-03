-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 03, 2024 at 11:48 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `asesmen`
--

-- --------------------------------------------------------

--
-- Table structure for table `bnba`
--

CREATE TABLE `bnba` (
  `id` int(11) NOT NULL,
  `nik` varchar(16) NOT NULL,
  `nokk` varchar(16) NOT NULL,
  `nama` varchar(24) NOT NULL,
  `alamat` varchar(100) NOT NULL,
  `status` int(11) NOT NULL DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bnba`
--

INSERT INTO `bnba` (`id`, `nik`, `nokk`, `nama`, `alamat`, `status`, `created_at`, `updated_at`) VALUES
(1, '9636197949115131', '7707807018188253', 'Bakiadi Mayasari', 'Gg. Ronggowarsito No. 2\nMojokerto, BE 31604', 0, '2024-10-29 01:13:03', '2024-10-29 01:13:03'),
(2, '4298694820927857', '6155529151708620', 'Aisyah Waskita, M.Ak', 'Gg. Sadang Serang No. 878\nMetro, KT 70296', 0, '2024-10-29 01:13:03', '2024-10-29 01:13:03'),
(3, '8083812829996764', '3997447460395527', 'drg. Vera Santoso, S.IP', 'Jl. H.J Maemunah No. 35\nManado, Sumatera Selatan 98529', 0, '2024-10-29 01:13:03', '2024-10-29 01:13:03'),
(4, '5172960341723517', '5254129167912122', 'Irnanto Rahimah', 'Gg. Gedebage Selatan No. 2\nMataram, MU 88052', 0, '2024-10-29 01:13:03', '2024-10-29 01:13:03'),
(5, '3691952500566343', '2576553711612055', 'Ir. Rendy Sudiati', 'Jalan Gardujati No. 2\nPadangpanjang, NT 63049', 0, '2024-10-29 01:13:03', '2024-10-29 01:13:03'),
(6, '2597506201120814', '8680975825653735', 'Ir. Jane Usamah', 'Gg. Cikutra Barat No. 155\nMakassar, Kalimantan Selatan 94810', 0, '2024-10-29 01:13:03', '2024-10-29 01:13:03'),
(7, '4661827650438863', '3911296842191845', 'Dinda Permadi', 'Gg. W.R. Supratman No. 80\nMedan, KB 27670', 0, '2024-10-29 01:13:03', '2024-10-29 01:13:03'),
(8, '3991766350826662', '9137126724337033', 'Nurul Susanti, S.Gz', 'Gang Setiabudhi No. 50\nMadiun, Sumatera Utara 24166', 0, '2024-10-29 01:13:03', '2024-10-29 01:13:03'),
(9, '1033749264650657', '9491548883481996', 'Ciaobella Prasasta', 'Jalan Pacuan Kuda No. 39\nBogor, Maluku 59185', 0, '2024-10-29 01:13:03', '2024-10-29 01:13:03'),
(10, '4832104097445395', '7969792377678532', 'Mila Mahendra', 'Jl. K.H. Wahid Hasyim No. 28\nMataram, SS 67680', 0, '2024-10-29 01:13:03', '2024-10-29 01:13:03');

-- --------------------------------------------------------

--
-- Table structure for table `hasil_asesmen`
--

CREATE TABLE `hasil_asesmen` (
  `bnba_id` int(11) NOT NULL,
  `anggota_kk` int(11) NOT NULL,
  `pendapatan` varchar(100) NOT NULL,
  `kondisi_rumah` varchar(20) NOT NULL,
  `sumber_air_minum` varchar(15) NOT NULL,
  `akses_listrik` varchar(15) NOT NULL,
  `kepemilikan_aset` varchar(15) NOT NULL,
  `pekerjaan` varchar(20) NOT NULL,
  `status_kepemilikan_rumah` varchar(20) NOT NULL,
  `penghasilan_dibawah_ump` int(11) NOT NULL,
  `aset_produktif` int(11) NOT NULL,
  `akses_pendidikan` int(11) NOT NULL,
  `akses_kesehatan` int(11) NOT NULL,
  `akses_sanitasi` int(11) NOT NULL,
  `akses_listrik_ump` int(11) NOT NULL,
  `rumah_tidak_layak_huni` int(11) NOT NULL,
  `skor_kemiskinan` int(11) NOT NULL,
  `kategori_asesmen` varchar(20) NOT NULL,
  `rekomendasi_bantuan` varchar(20) NOT NULL,
  `created_by` int(11) NOT NULL,
  `updated_by` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `session`
--

CREATE TABLE `session` (
  `user_id` int(11) NOT NULL,
  `token` varchar(100) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(24) NOT NULL,
  `password` varchar(100) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `created_at`) VALUES
(3, 'fho1', '829b36babd21be519fa5f9353daf5dbdb796993e', '2024-10-29 03:11:43');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bnba`
--
ALTER TABLE `bnba`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hasil_asesmen`
--
ALTER TABLE `hasil_asesmen`
  ADD KEY `asesmen_bnba` (`bnba_id`),
  ADD KEY `asesmen_user1` (`created_by`),
  ADD KEY `asesmen_user2` (`updated_by`);

--
-- Indexes for table `session`
--
ALTER TABLE `session`
  ADD KEY `user_session` (`user_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bnba`
--
ALTER TABLE `bnba`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `hasil_asesmen`
--
ALTER TABLE `hasil_asesmen`
  ADD CONSTRAINT `asesmen_bnba` FOREIGN KEY (`bnba_id`) REFERENCES `bnba` (`id`),
  ADD CONSTRAINT `asesmen_user1` FOREIGN KEY (`created_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `asesmen_user2` FOREIGN KEY (`updated_by`) REFERENCES `user` (`id`);

--
-- Constraints for table `session`
--
ALTER TABLE `session`
  ADD CONSTRAINT `user_session` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
