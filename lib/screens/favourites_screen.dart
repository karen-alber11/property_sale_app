import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import '../models/property.dart';
import '../widgets/property_card.dart';
import '../cubit/favourites_cubit.dart';

class FavoritesScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return BlocBuilder<FavoritesCubit, List<Property>>(
      builder: (context, favorites) {
        return Scaffold(
          appBar: AppBar(
            title: Text("Favorites"),
            backgroundColor: Colors.teal,
          ),
          body: favorites.isEmpty
              ? Center(child: Text("No favorites added yet"))
              : ListView.builder(
            itemCount: favorites.length,
            itemBuilder: (context, index) {
              final property = favorites[index];
              return PropertyCard(
                property: property,
                isFavorite: true,
                onFavoriteToggle: () {
                  context.read<FavoritesCubit>().removeFavorite(property);
                },
                onTap: () {
                  // Optional: Navigate to property details page
                },
              );
            },
          ),
        );
      },
    );
  }
}
