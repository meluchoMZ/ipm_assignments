// IPM P2 task2
// Authors:
// Miguel Blanco Godón
// Christian David Outeda García
// Version 0.2 /16/11/2020

import 'package:face_scanner/screens/main_view.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:face_scanner/models/model_io.dart';

void main() {
  runApp(
    ChangeNotifierProvider(
      create: (context) => ModelIO(),
      child: App(),
    ),
  );
}


class App extends StatelessWidget {
  @override
  Widget build(BuildContext) {
    return MaterialApp(
      title: 'Face scanner',
      theme: ThemeData(
        primarySwatch: Colors.indigo,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: MainView(title: 'Face scanner'),
    );
  }
}

