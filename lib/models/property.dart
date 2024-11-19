class Property {
  final String type;
  final String title;
  final String description;
  final String link;
  final String datePublished;

  Property({
    required this.type,
    required this.title,
    required this.description,
    required this.link,
    required this.datePublished,
  });

  // Add a method to calculate the relative date
  String get relativeDate {
    final publishedDate = DateTime.parse(datePublished);
    final today = DateTime.now();

    if (publishedDate.year == today.year &&
        publishedDate.month == today.month &&
        publishedDate.day == today.day) {
      return "Pinned today";
    } else {
      return "Not pinned today";
    }
  }

  // Add a fromJson factory for API parsing
  factory Property.fromJson(Map<String, dynamic> json) {
    return Property(
      type: json['type'] as String,
      title: json['title'] as String,
      description: json['description'] as String,
      link: json['link'] as String,
      datePublished: json['datePublished'] as String,
    );
  }

  // Add toJson for potential serialization if needed
  Map<String, dynamic> toJson() {
    return {
      'type': type,
      'title': title,
      'description': description,
      'link': link,
      'datePublished': datePublished,
    };
  }

  // Add a fromMap method for database integration
  factory Property.fromMap(Map<String, dynamic> map) {
    return Property(
      type: map['type'] as String,
      title: map['title'] as String,
      description: map['description'] as String,
      link: map['link'] as String,
      datePublished: map['datePublished'] as String,
    );
  }

  // Add a toMap method for database integration
  Map<String, dynamic> toMap() {
    return {
      'type': type,
      'title': title,
      'description': description,
      'link': link,
      'datePublished': datePublished,
    };
  }
}
