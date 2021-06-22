// IPM P2 task 2
// Authors:
// Miguel Blanco Godón
// Christian David Outeda García
// Version 0.2 /16/11/2020

class Face {
  // Attributes
  String _age = null;
  String _sex = null;
  String _race = null;
  List<String> _coordinates = null;

  // Constructor
  Face(String age, String sex, String race , int h, int w, int xmax, int xmin,
      int ymax, int ymin) {
    _age = age;
    _sex = sex;
    _race = race;
    _coordinates = ['$h', '$w', '$xmax', '$xmin', '$ymax', '$ymin'];
  }

  // Getters
  String get age => this._age;
  String get sex => this._sex;
  String get race => this._race;
  List<String> get coordinates => this._coordinates;
}