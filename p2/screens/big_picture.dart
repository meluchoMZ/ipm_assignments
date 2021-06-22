// IPM P2 task 2
// Authors:
// Miguel Blanco Godón
// Christian David Outeda García
// Version 0.2 /16/11/2020

import 'package:flutter/material.dart';
import 'package:photo_view/photo_view.dart';

class BigPicture extends StatelessWidget {
  // Attributes

  final ImageProvider image;

  // Constructor
  BigPicture({this.image});


  // Build
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Face scanner")),
      body: Center(
        child: PhotoView(
          imageProvider: image,
          enableRotation: true,
        ),
      ),
    );
  }
}