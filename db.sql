USE [Weather]
GO
/****** Object:  Table [dbo].[weather]    Script Date: 14/05/2024 9:48:07 CH ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[weather](
	[city] [nchar](10) NULL,
	[temperature] [nchar](10) NULL,
	[pressure] [nchar](10) NULL,
	[humidity] [nchar](10) NULL,
	[wind_speed] [nchar](10) NULL,
	[description] [nchar](10) NULL
) ON [PRIMARY]
GO
/****** Object:  StoredProcedure [dbo].[SP_weather]    Script Date: 14/05/2024 9:48:07 CH ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[SP_weather]
    @city NVARCHAR(50),
    @temperature DECIMAL(18,2),
    @pressure INT,
    @humidity INT,
    @wind_speed DECIMAL(18,2),
    @description NVARCHAR(100)
AS
BEGIN
    DECLARE @json NVARCHAR(MAX);

    SET @json = N'{"city":"' + @city + '","temperature":' + CONVERT(NVARCHAR(50), @temperature) + ',"pressure":' + CONVERT(NVARCHAR(50), @pressure) + ',"humidity":' + CONVERT(NVARCHAR(50), @humidity) + ',"wind_speed":' + CONVERT(NVARCHAR(50), @wind_speed) + ',"description":"' + @description + '"}';

    SELECT @json AS json;
END;
GO
