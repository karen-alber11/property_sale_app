import 'package:flutter/material.dart';
import '../models/property.dart';
import '../core/fonts.dart';

class DetailsScreen extends StatelessWidget {
  final Property property;

  const DetailsScreen({Key? key, required this.property}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Details", style: AppFonts.large),
        backgroundColor: Colors.teal,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(property.type, style: AppFonts.small),
            SizedBox(height: 8),
            Text(property.title, style: AppFonts.large),
            SizedBox(height: 8),
            Text(property.description, style: AppFonts.medium),
            SizedBox(height: 8),
            Text("Link: ${property.link}", style: AppFonts.medium, overflow: TextOverflow.ellipsis),
            SizedBox(height: 8),
            Text("Published: ${property.datePublished}", style: AppFonts.small),
          ],
        ),
      ),
    );
  }
}
