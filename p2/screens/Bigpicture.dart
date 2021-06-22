import 'package:flutter/material.dart';
import 'package:photo_view/photo_view.dart';

class BigPicture extends StatelessWidget {
  BigPicture({this.image});
  final ImageProvider image;
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
