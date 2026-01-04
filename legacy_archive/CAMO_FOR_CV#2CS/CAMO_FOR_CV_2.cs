using System;
using System.Data.SqlClient;

public class DatabaseManager {
    private readonly string _connectionString;

    public DatabaseManager() {
        _connectionString = @"Server=(localdb)\MSSQLLocalDB;Database=CargoDB;Integrated Security=true;";
        InitializeDatabase();
    }

    private void InitializeDatabase() {
        using (var connection = new SqlConnection(_connectionString)) {
            connection.Open();
            
            // Veritabanı yoksa oluştur
            var createDbCmd = new SqlCommand(
                "IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'CargoDB') " +
                "CREATE DATABASE CargoDB", connection);
            createDbCmd.ExecuteNonQuery();

            // Tablo yoksa oluştur
            var createTableCmd = new SqlCommand(
                @"USE CargoDB;
                IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Cargos' AND xtype='U')
                CREATE TABLE Cargos (
                    Id INT IDENTITY(1,1) PRIMARY KEY,
                    CargoId NVARCHAR(50) NOT NULL,
                    VideoPath NVARCHAR(255) NOT NULL,
                    LabelText NVARCHAR(MAX) NOT NULL,
                    CreatedAt DATETIME DEFAULT GETDATE()
                )", connection);
            createTableCmd.ExecuteNonQuery();
        }
    }

    public void SaveCargoInfo(string cargoId, string videoPath, string labelText) {
        using (var connection = new SqlConnection(_connectionString)) {
            connection.Open();
            var cmd = new SqlCommand(
                @"USE CargoDB;
                INSERT INTO Cargos (CargoId, VideoPath, LabelText)
                VALUES (@cargoId, @videoPath, @labelText)", connection);
            
            cmd.Parameters.AddWithValue("@cargoId", cargoId);
            cmd.Parameters.AddWithValue("@videoPath", videoPath);
            cmd.Parameters.AddWithValue("@labelText", labelText);
            cmd.ExecuteNonQuery();
        }
    }

    public void GetCargoInfo(string cargoId) {
        using (var connection = new SqlConnection(_connectionString)) {
            connection.Open();
            var cmd = new SqlCommand(
                @"USE CargoDB;
                SELECT * FROM Cargos WHERE CargoId = @cargoId", connection);
            
            cmd.Parameters.AddWithValue("@cargoId", cargoId);
            var reader = cmd.ExecuteReader();
            
            while (reader.Read()) {
                Console.WriteLine($"Video: {reader["VideoPath"]}, Metin: {reader["LabelText"]}");
            }
        }
    }
}
