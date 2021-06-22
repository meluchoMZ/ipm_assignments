//IPM P2 task 2
// Authors:
// Miguel Blanco Godón
// Chrisitian David Outeda García
// Version 0.2 /16/11/2020

import 'package:flutter/material.dart';
import 'package:face_scanner/models/face.dart';

class FacesList extends StatelessWidget {
  List<Face> facesList;
  bool isTablet;
  double _title_size = 30;
  double _subtitle_size = 25;
  double _body_size = 19;
  FacesList({this.facesList, this.isTablet});
  @override
  Widget build(BuildContext context) {
    if (isTablet) {
      _title_size = _title_size + 15;
      _subtitle_size = _subtitle_size + 15;
      _body_size = _body_size + 15;
    }
    return ListView.separated(
      padding: const EdgeInsets.all(8),
      itemCount: facesList.length,
      itemBuilder: (BuildContext context, int index) {
        return Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget> [
              Text(
                "Face ${index+1}",
                style: TextStyle(
                  fontFamily: 'RobotoSlab',
                  fontWeight: FontWeight.w600,
                  fontSize: _title_size,
                ),
              ),
              Text(
                "Attributes",
                style: TextStyle(
                  fontFamily: 'RobotoSlab',
                  fontWeight: FontWeight.w500,
                  fontSize: _subtitle_size,
                ),
              ),
              Row (mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget> [
                Text("Age: ",style: TextStyle(
                  fontFamily: 'OpenSans',
                  fontWeight: FontWeight.bold,
                  fontSize: _body_size,
                ),),
                Text("${facesList[index].age}",
                  style: TextStyle(
                  fontSize: _body_size,
                  ),
                ),
                ],
              ),
              Row (mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget> [
                  Text("Gender: ",style: TextStyle(
                    fontFamily: 'OpenSans',
                    fontWeight: FontWeight.bold,
                    fontSize: _body_size,
                  ),),
                  Text("${facesList[index].sex}",
                    style: TextStyle(
                      fontSize: _body_size,
                    ),
                  ),
                ],
              ),
              Row (mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget> [
                  Text("Ethnicity: ",style: TextStyle(
                    fontFamily: 'OpenSans',
                    fontWeight: FontWeight.bold,
                    fontSize: _body_size,
                  ),),
                  Text("${facesList[index].race}",
                    style: TextStyle(
                      fontSize: _body_size,
                    ),
                  ),
                ],
              ),
              Text(
                "Coordinates",
                style: TextStyle(
                  fontFamily: 'RobotoSlab',
                  fontWeight: FontWeight.w500,
                  fontSize: _subtitle_size,
                ),
              ),
              Row (mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget> [
                  Text("Height: ",style: TextStyle(
                    fontFamily: 'OpenSans',
                    fontWeight: FontWeight.bold,
                    fontSize: _body_size,
                  ),),
                  Text("${facesList[index].coordinates[0]}",
                    style: TextStyle(
                      fontSize: _body_size,
                    ),
                  ),
                ],
              ),
              Row (mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget> [
                  Text("Width: ",style: TextStyle(
                    fontFamily: 'OpenSans',
                    fontWeight: FontWeight.bold,
                    fontSize: _body_size,
                  ),),
                  Text("${facesList[index].coordinates[1]}",
                    style: TextStyle(
                      fontSize: _body_size,
                    ),
                  ),
                ],
              ),
              Row (mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget> [
                  Text("XMAX: ",style: TextStyle(
                    fontFamily: 'OpenSans',
                    fontWeight: FontWeight.bold,
                    fontSize: _body_size,
                  ),),
                  Text("${facesList[index].coordinates[2]}",
                    style: TextStyle(
                      fontSize: _body_size,
                    ),
                  ),
                ],
              ),
              Row (mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget> [
                  Text("XMIN: ",style: TextStyle(
                    fontFamily: 'OpenSans',
                    fontWeight: FontWeight.bold,
                    fontSize: _body_size,
                  ),),
                  Text("${facesList[index].coordinates[3]}",
                    style: TextStyle(
                      fontSize: _body_size,
                    ),
                  ),
                ],
              ),
              Row (mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget> [
                  Text("YMAX: ",style: TextStyle(
                    fontFamily: 'OpenSans',
                    fontWeight: FontWeight.bold,
                    fontSize: _body_size,
                  ),),
                  Text("${facesList[index].coordinates[4]}",
                    style: TextStyle(
                      fontSize: _body_size,
                    ),
                  ),
                ],
              ),
              Row (mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget> [
                  Text("YMIN: ",style: TextStyle(
                    fontFamily: 'OpenSans',
                    fontWeight: FontWeight.bold,
                    fontSize: _body_size,
                  ),),
                  Text("${facesList[index].coordinates[5]}",
                    style: TextStyle(
                      fontSize: _body_size,
                    ),
                  ),
                ],
              ),
            ],
          ),
        );
      },
      separatorBuilder: (BuildContext context, int index) => const Divider(),
    );
  }
}
