-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 26, 2022 at 02:24 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `book_id` int(5) NOT NULL,
  `book_name` varchar(100) NOT NULL,
  `author` varchar(50) NOT NULL,
  `cost` int(10) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `status` varchar(10) NOT NULL DEFAULT 'พร้อมขาย',
  `time_add` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`book_id`, `book_name`, `author`, `cost`, `description`, `status`, `time_add`) VALUES
(5, 'Alphabet of Thorn อาลักษณ์แห่งเรน', 'แพทริเซีย แมคคิลลิป', 365, 'เนอเพนธี\nอาลักษณ์ประจำห้องสมุดหลวงที่อยู่ลึกลงไปในหน้าผาใต้\nพระราชวัง ณ ริมขอบโลก มีหน้าที่แปลหนังสื', 'พร้อมขาย', '2022-10-24'),
(6, 'THE CHANGELING SEA ปาฏิหาริย์แห่งทะเล', 'แพทริเซีย แมคคิลลิป', 225, 'สุดยอดผลงานของผู้เขียน The Forgotten Beasts of Eld\n\nทะเลพรากทุกสิ่งที่เพริรัก เธอจึงตัดสินใจแก้แค้น ', 'พร้อมขาย', '2022-10-24'),
(7, 'The Forgotten Beasts of Eld สัตว์วิเศษแห่งเอลด์', 'แพทริเซีย แมคคิลลิป', 295, 'นามของสัตว์โบราณอันแสนวิเศษที่มนุษย์ลืมเลือนไปกำลังจะกลับมา...\n\nซีเบล จอมเวทแห่งภูเขาเอลด์ ใช้ชีวิตอ', 'พร้อมขาย', '2022-10-24'),
(8, 'สกันดาร์กับจอมโจรขโมยยูนิคอร์น', 'A.F. Steadman', 345, 'สกันดาร์กับจอมโจรขโมยยูนิคอร์น\n\n  \"สกันดาร์ สมิท\" ใฝ่ฝันที่จะออกจากแผ่นดินใหญ่ไปฝึกยังเกาะลึกลับ ดิน', 'พร้อมขาย', '2022-10-24'),
(27, 'หายนะแห่งมนตร์อนธการ\n', 'SCHWAB, V.E.', 339, 'หายนะแห่งมนตร์อนธการ\n\nประตูเชื่อมต่อระหว่างโลกคู่ขนานทั้งสี่ปิดตายลงด้วยเหตุผลบางอย่าง\nนับแต่นั้นเป็', 'พร้อมขาย', '2022-10-24'),
(30, 'asdasd', 'asdasdasdas', 1000, 'dasdas', 'หมด', '2022-10-24'),
(31, 'เชิญร่ำสุรา เล่ม 5', 'ถังจิ่วชิง', 425, 'รายละเอียด : เชิญร่ำสุรา เล่ม 5\nเชิญร่ำสุรา เล่ม 5\n\n\"เซียนเซิงคืนชีวิตนี้ให้ข้าแล้ว อาเหย่\"\nเสิ่นเจ๋', 'พร้อมขาย', '2022-10-24'),
(32, '111111111', '222', 3, 'asdsadasd', 'พร้อมขาย', '2022-10-26'),
(33, 'zzzzz', '2', 3, '4', 'พร้อมขาย', '2022-10-26');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(10) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `displayname` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`book_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `book_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
