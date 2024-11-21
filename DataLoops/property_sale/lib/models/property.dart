class Property {
  final String type;
  final String title;
  final String description;
  final String link;
  final String datePublished;
  final String dateRelative;

  Property({
    required this.type,
    required this.title,
    required this.description,
    required this.link,
    required this.datePublished,
    required this.dateRelative,
  });

  // Factory constructor for API parsing
  factory Property.fromJson(Map<String, dynamic> json) {
    return Property(
      type: json['type'] as String? ?? 'Unknown',
      title: json['title'] as String? ?? 'Untitled',
      description: json['description'] as String? ?? 'No description',
      link: json['link'] as String? ?? 'No link',
      datePublished: json['datePublished'] as String? ?? '',
      dateRelative: json['dateRelative'] as String? ?? 'No dateRelative',
    );
  }

  // Convert to JSON for serialization
  Map<String, dynamic> toJson() {
    return {
      'type': type,
      'title': title,
      'description': description,
      'link': link,
      'datePublished': datePublished,
      'dateRelative': dateRelative,
    };
  }

  // Factory constructor for database integration
  factory Property.fromMap(Map<String, dynamic> map) {
    return Property(
      type: map['type'] as String? ?? 'Unknown',
      title: map['title'] as String? ?? 'Untitled',
      description: map['description'] as String? ?? 'No description',
      link: map['link'] as String? ?? 'No link',
      datePublished: map['datePublished'] as String? ?? '',
      dateRelative: map['dateRelative'] as String? ?? 'No dateRelative',
    );
  }

  // Convert to Map for database integration
  Map<String, dynamic> toMap() {
    return {
      'type': type,
      'title': title,
      'description': description,
      'link': link,
      'datePublished': datePublished,
      'dateRelative': dateRelative,
    };
  }

  // Parse a List<Map<String, dynamic>> into List<Property>
  static List<Property> fromList(List<Map<String, dynamic>> list) {
    return list
        .where((map) => map is Map<String, dynamic>)
        .map((map) => Property.fromMap(map))
        .toList();
  }
}
