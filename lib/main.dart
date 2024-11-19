import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'screens/home_screen.dart';
import 'screens/favourites_screen.dart';
import 'cubit/favourites_cubit.dart';
import 'services/api_service.dart';
import 'models/property.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // Fetch properties from API
  final apiService = ApiService();
  final List<Property> properties = await apiService.fetchProperties();

  runApp(MyApp(properties: properties));
}

class MyApp extends StatelessWidget {
  final List<Property> properties;

  const MyApp({Key? key, required this.properties}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return BlocProvider(
      create: (context) => FavoritesCubit()..loadFavorites(),
      child: MaterialApp(
        title: 'Real Estate App',
        theme: ThemeData(primarySwatch: Colors.teal),
        home: MyHomePage(properties: properties),
      ),
    );
  }
}

class MyHomePage extends StatefulWidget {
  final List<Property> properties;

  const MyHomePage({Key? key, required this.properties}) : super(key: key);

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _selectedIndex = 0;

  @override
  Widget build(BuildContext context) {
    final List<Widget> _pages = [
      HomeScreen(properties: widget.properties),
      FavoritesScreen(),
    ];

    return Scaffold(
      body: _pages[_selectedIndex],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _selectedIndex,
        onTap: (index) => setState(() => _selectedIndex = index),
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.home), label: 'Home'),
          BottomNavigationBarItem(icon: Icon(Icons.star), label: 'Favorites'),
        ],
      ),
    );
  }
}
