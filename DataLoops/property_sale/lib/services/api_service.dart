import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/property.dart';

class ApiService {
  final String baseUrl = "http://your-python-backend-endpoint.com/properties";

  Future<List<Property>> fetchProperties() async {
    final response = await http.get(Uri.parse(baseUrl));

    if (response.statusCode == 200) {
      final List<dynamic> jsonData = json.decode(response.body);
      return jsonData.map((json) => Property.fromJson(json)).toList();
    } else {
      throw Exception('Failed to load properties');
    }
  }
}
