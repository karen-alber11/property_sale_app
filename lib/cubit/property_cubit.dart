import 'package:bloc/bloc.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import '../models/property.dart';
import 'property_state.dart';

class PropertyCubit extends Cubit<PropertyState> {
  PropertyCubit() : super(PropertyInitial());

  Future<void> fetchProperties() async {
    emit(PropertyLoading());
    try {
      final response = await http.get(Uri.parse('http://localhost:5000/properties'));
      if (response.statusCode == 200) {
        List jsonData = jsonDecode(response.body);
        List<Property> properties = jsonData.map((item) => Property.fromJson(item)).toList();
        emit(PropertyLoaded(properties));
      } else {
        emit(PropertyError('Failed to load properties'));
      }
    } catch (e) {
      emit(PropertyError(e.toString()));
    }
  }
}
