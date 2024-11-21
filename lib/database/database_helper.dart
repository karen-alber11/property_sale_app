import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';
import '../models/property.dart';

class DatabaseHelper {
  static final DatabaseHelper _instance = DatabaseHelper._internal();

  factory DatabaseHelper() => _instance;

  DatabaseHelper._internal();

  static Database? _database;

  Future<Database> get database async {
    if (_database != null) return _database!;
    _database = await _initDatabase();
    return _database!;
  }

  Future<Database> _initDatabase() async {
    final dbPath = await getDatabasesPath();
    return openDatabase(
      join(dbPath, 'favorites.db'),
      version: 2,  // Incremented version to trigger schema upgrade
      onCreate: (db, version) {
        // Initial database creation with the new schema
        return db.execute(''' 
          CREATE TABLE favorites(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            title TEXT,
            description TEXT,
            link TEXT UNIQUE,
            datePublished TEXT,
            dateRelative TEXT  // Adding dateRelative column
          )
        ''');
      },
      // onUpgrade: (db, oldVersion, newVersion) {
      //   // Handling database upgrade
      //   if (oldVersion < 2) {
      //     // Adding the dateRelative column if it's missing
      //     db.execute('''
      //       ALTER TABLE favorites ADD COLUMN dateRelative TEXT;
      //     ''');
      //   }
      // },
    );
  }

  Future<void> addFavorite(Property property) async {
    final db = await database;
    await db.insert(
      'favorites',
      property.toMap(),
      conflictAlgorithm: ConflictAlgorithm.replace,
    );
  }

  Future<List<Property>> getFavorites() async {
    final db = await database;
    final List<Map<String, dynamic>> maps = await db.query('favorites');
    return List.generate(maps.length, (i) {
      return Property.fromMap(maps[i]);
    });
  }

  Future<void> removeFavorite(String title) async {
    final db = await database;
    await db.delete(
      'favorites',
      where: 'title = ?',
      whereArgs: [title],
    );
  }
}
