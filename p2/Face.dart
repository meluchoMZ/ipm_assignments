import 'package:flutter/material.dart';

class Face {
  String _age = null;
  String _sex = null;
  String _race = null;
  List<String> _coordinates = null;

  Face(String age, String sex, String race, int h, int w, int xmax,
      int xmin, int ymax, int ymin) {
    _age = age;
    _sex = sex;
    _race = race;
    _coordinates = ['$h', '$w', '$xmax', '$xmin', '$ymax', '$ymin'];
  }

  String get age => this._age;

  String get sex => this._sex;

  String get race => this._race;

  List<String> get coordinates => this._coordinates;
}