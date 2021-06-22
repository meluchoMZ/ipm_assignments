// IPM P2 task 2
// Authors:
// Miguel Blanco Godón
// Christian David Outeda García
// Version 0.2 /16/11/2020

import 'dart:io';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:dio/dio.dart';
import 'package:face_scanner/models/face.dart';
import 'package:flutter/foundation.dart';

class ModelIO extends ChangeNotifier {
  // Attributes
  List<Face> _facesList;
  bool _error = false;
  String _errorTitle;
  String _errorSubtitle;
  // Methods
  ModelIO() {
    _facesList = [];
  }

  // Getters
  List<Face> get facesList => _facesList;
  bool get error => _error;
  String get errorTitle => _errorTitle;
  String get errorSubtitle => _errorSubtitle;

  void uploadAndGetData(File picture) async {
    var pictureBytes = await picture.readAsBytes();
    var up;
    var dio = new Dio();
    var base64Enc = base64Encode(pictureBytes);
    FormData fd = new FormData.fromMap(
      {'image_base64' : base64Enc}
    );
    try {
      up = await Dio().post(
        'https://api.imagga.com/v2/uploads',
        options: Options(
          /* removed authorization for security reasons */
        ),
        data: fd,
      );
    } catch (e) {
      _error = true;
      _errorTitle = "Cannot upload picture";
      _errorSubtitle = "Please check your internet connection";
      notifyListeners();
      return;
    }

    if (up == null) {
      _error = true;
      _errorTitle = "Cannot upload picture";
      _errorSubtitle = "Please check your internet connection and try again";
      notifyListeners();
      return;
    }

    var upload_id = up.data['result']['upload_id'];
    var temp = await http.get(
      'https://api.imagga.com/v2/faces/detections?return_face_attributes=1&image_upload_id=$upload_id',
      headers: <String, String> {
                  /* removed authorization for security reasons */
      }
    );

    if (jsonDecode(temp.body)['status']['type'] == 'error') {
      _facesList.removeRange(0, _facesList.length);
      _error = true;
      _errorTitle = "Error";
      _errorSubtitle = "Something went wrong. Please try again.";
      notifyListeners();
      return;
    }

    var decoded = jsonDecode(temp.body);
    var faces = decoded['result']['faces'];
    if (faces.length == 0) {
      _facesList.removeRange(0, _facesList.length);
      _error = true;
      _errorTitle = "Ups!";
      _errorSubtitle = "We couldn\'t find any face in this picture";
      notifyListeners();
      return;
    }

    // cleaning the faces list
    _facesList.removeRange(0, _facesList.length);

    // filling faces list
    for (int i = 0; i < faces.length; i++) {
      List coordinates = [];
      var enc = jsonEncode(faces[i]);
      var eCord = jsonDecode(enc);
      var eeCord = jsonDecode(jsonEncode(jsonDecode(enc)['coordinates']));
      coordinates.add(eeCord['height']);
      coordinates.add(eeCord['width']);
      coordinates.add(eeCord['xmax']);
      coordinates.add(eeCord['xmin']);
      coordinates.add(eeCord['ymax']);
      coordinates.add(eeCord['ymin']);
      var at = eCord['attributes'];
      List<String> attributes = ['age', 'gender', 'race'];
      for (int j = 0; j < at.length; j++) {
        attributes[j] = at[j]['label'];
      }
      _facesList.add(
        Face(attributes[0], attributes[1], attributes[2],
        coordinates[0], coordinates[1], coordinates[2], coordinates[3],
        coordinates[4], coordinates[5])
      );
    }
    _error = false;
    notifyListeners();
  }

  void dismissError() {
    if (!error) return;
    _error = false;
    notifyListeners();
  }
}
