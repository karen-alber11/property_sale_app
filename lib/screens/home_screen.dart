import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import '../models/property.dart';
import '../widgets/property_card.dart';
import '../widgets/property_details.dart';
import '../cubit/favourites_cubit.dart';

class HomeScreen extends StatefulWidget {
  final List<Property> properties;

  const HomeScreen({Key? key, required this.properties}) : super(key: key);

  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  String _selectedTab = "Pinned";

  @override
  Widget build(BuildContext context) {
    return BlocBuilder<FavoritesCubit, List<Property>>(
      builder: (context, favorites) {
        final filteredProperties = _selectedTab == "Pinned"
            ? widget.properties.where((p) => p.relativeDate == "Pinned today").toList()
            : widget.properties.where((p) => p.relativeDate != "Pinned today").toList();

        return Scaffold(
          appBar: AppBar(
            title: const Text("Home"),
            backgroundColor: Colors.teal,
          ),
          body: Column(
            children: [
              // Upper navigation bar under the app bar
              Container(
                color: Colors.teal[100],
                padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: ["Pinned", "Latest"].map((tab) {
                    return GestureDetector(
                      onTap: () => setState(() => _selectedTab = tab),
                      child: Container(
                        margin: const EdgeInsets.symmetric(horizontal: 10),
                        padding: const EdgeInsets.symmetric(vertical: 8, horizontal: 20),
                        decoration: BoxDecoration(
                          color: _selectedTab == tab ? Colors.teal : Colors.transparent,
                          borderRadius: BorderRadius.circular(20),
                        ),
                        child: Text(
                          tab,
                          style: TextStyle(
                            color: _selectedTab == tab ? Colors.white : Colors.teal,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ),
                    );
                  }).toList(),
                ),
              ),
              Expanded(
                child: ListView.builder(
                  itemCount: filteredProperties.length,
                  itemBuilder: (context, index) {
                    final property = filteredProperties[index];
                    final isFavorite =
                    favorites.any((fav) => fav.title == property.title);

                    return PropertyCard(
                      property: property,
                      isFavorite: isFavorite,
                      onFavoriteToggle: () {
                        if (isFavorite) {
                          context.read<FavoritesCubit>().removeFavorite(property);
                        } else {
                          context.read<FavoritesCubit>().addFavorite(property);
                        }
                      },
                      onTap: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (_) => PropertyDetails(property: property),
                          ),
                        );
                      },
                    );
                  },
                ),
              ),
            ],
          ),
        );
      },
    );
  }
}
