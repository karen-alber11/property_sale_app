import 'package:flutter_bloc/flutter_bloc.dart';
import '../models/property.dart';
import '../database/database_helper.dart';

class FavoritesCubit extends Cubit<List<Property>> {
  final DatabaseHelper databaseHelper = DatabaseHelper();

  FavoritesCubit() : super([]);

  void loadFavorites() async {
    final favorites = await databaseHelper.getFavorites();
    emit(favorites);
  }

  void addFavorite(Property property) async {
    await databaseHelper.addFavorite(property);
    loadFavorites(); // Reload favorites to update the state
  }

  void removeFavorite(Property property) async {
    await databaseHelper.removeFavorite(property.title);
    loadFavorites(); // Reload favorites to update the state
  }
}
