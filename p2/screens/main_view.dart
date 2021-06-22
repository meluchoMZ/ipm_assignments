//IPM P2 task 2
// Authors:
// Miguel Blanco Godón
// Chrisitian David Outeda García 
// Version 0.2 /16/11/2020

import 'dart:ui';

import 'package:flutter/material.dart';
import 'package:face_scanner/models/face.dart';
import 'package:face_scanner/models/model_io.dart';
import 'package:face_scanner/screens/big_picture.dart';
import 'package:progress_dialog/progress_dialog.dart';
import 'dart:io';
import 'package:image_picker/image_picker.dart';
import 'package:provider/provider.dart';
import 'package:face_scanner/screens/widgets.dart';


class MainView extends StatefulWidget {
  MainView({Key key, this.title}) : super(key:key);
  final String title;

  @override
  _MainView createState() => _MainView();
}

class _MainView extends State<MainView> {
  // Attributes
  static ProgressDialog _dialog;
  File _picture = null;
  double _height;
  double _width;
  // Methods

  // Alert Dialog
  Future<void> _showAlertDialog(String title, String subtitle) async {
    return showDialog<void>(
      context: context,
      barrierDismissible: false,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text(title),
          content: SingleChildScrollView(
            child: ListBody(
              children: <Widget>[
                Text(subtitle),
              ],
            ),
          ),
          actions: <Widget>[
            TextButton(
              child: Text('Ok'),
              onPressed: () {
                Navigator.of(context).pop();
              },
            ),
          ],
        );
      },
    );
  }

  Widget Portrait(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Container(
          decoration: BoxDecoration(
            gradient: LinearGradient(
              begin: Alignment.topRight,
              end: Alignment.bottomLeft,
                colors: [Colors.blueAccent, Colors.black38])),
      child: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget> [
            SizedBox(
              height: _height,
              width: _width,
              child: _picture == null
                  ? Center(child: new Text('Please select or take a photo!',style: TextStyle(
                fontFamily: 'Shrikhand',
                fontSize: 25,

              ),))
                  : Center(
                child: GestureDetector(
                  child: Image.file(_picture),
                  onTap: (() async {
                    Navigator.of(context).push(
                      MaterialPageRoute(
                        builder: (BuildContext context) {
                          return BigPicture(image: new Image.file(_picture).image);
                        },
                      ),
                    );
                  }),
                ),
              ),
            ),
            Text(
              "DATA:",
              style: TextStyle(
                fontSize: 35,
                fontWeight: FontWeight.w800,
              ),
            ),
            Expanded(
              child: Container(
                height: 200,
                child: Center(
                  child: Consumer<ModelIO> (
                      builder: (context, io, child) {
                        print("ERROR BEFORE IF: ${io.error}");
                        if (io.error) {
                          Provider.of<ModelIO>(context, listen: false).dismissError();
                          print("ERROR AFTER IF: ${io.error}");
                          Future.delayed(Duration(seconds:1)).then((value) {
                            _dialog.hide();

                            WidgetsBinding.instance.addPostFrameCallback((_) {
                              print("BEFORE SHOW ALERT DIALOG");
                              _showAlertDialog(io.errorTitle, io.errorSubtitle);
                              print("AFTER SHOW ALERT DIALOG");
                              return;
                            });
                            Provider.of<ModelIO>(context, listen: false).dismissError();
                          });

                          return Text("No faces found",style: TextStyle(
                            fontFamily: 'OpenSans',
                            fontSize: 20,
                          ),);
                        } else {
                          if(io.facesList.length == 0) {
                            _dialog.hide();
                            return Text("No faces found",style: TextStyle(
                              fontFamily: 'OpenSans',
                              fontSize: 20,
                            ),);
                          } else {
                            _dialog.hide();
                            return FacesList(facesList: io.facesList, isTablet: false);
                          }}
                      }
                  ),
                ),
              ),), // expanded
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              mainAxisSize: MainAxisSize.max,
              children: <Widget>[
                IconButton(
                    iconSize: 80,
                    icon: Icon(Icons.add_a_photo),
                    onPressed: () {
                      _cameraButtonHandler();
                    }
                ),
                IconButton(
                    iconSize: 90,
                    icon: Icon(Icons.add_photo_alternate),
                    onPressed: () {
                      _galleryButtonHandler();
                    }
                ),
              ],
            ),
          ],
        ),
      ),
      ),
    ),
    );
  }

  Widget Landscape(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
    child: Container(
    decoration: BoxDecoration(
        gradient: LinearGradient(
        begin: Alignment.topRight,
        end: Alignment.bottomLeft,
        colors: [Colors.blueAccent, Colors.black38])),
      child: Center(
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Column(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: <Widget>[
                Expanded(
                  child: SizedBox(
                  height: 200,
                  width: 300,
                  child: _picture == null
                      ? Center(child: new Text('Please select or take a photo!',style:TextStyle(
                    fontSize: 25,
                    fontFamily: 'Shrikhand',
                  )
                  ))
                      : Center(
                    child: GestureDetector(
                      child: Container(
                        child: Image.file(_picture),
                      ),
                      onTap: (() async {
                        Navigator.of(context).push(
                          MaterialPageRoute(
                            builder: (BuildContext context) {
                              return BigPicture(
                                  image: new Image.file(_picture).image);
                            },
                          ),
                        );
                      }),
                    ),
                  ),
                ),),
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  mainAxisSize: MainAxisSize.max,
                  children: <Widget>[
                    IconButton(
                        iconSize: 80,
                        icon: Icon(Icons.add_a_photo),
                        onPressed: () {
                          _cameraButtonHandler();
                        }
                    ),
                    IconButton(
                        iconSize: 90,
                        icon: Icon(Icons.add_photo_alternate),
                        onPressed: () {
                          _galleryButtonHandler();
                        }
                    ),
                  ],
                ),
              ],
            ),
            Expanded(
              child:Column(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: <Widget>[
                  Text(
                    "DATA:",
                    style: TextStyle(
                      fontSize: 25,
                      fontWeight: FontWeight.w800,
                    ),
                  ),
                  Container(
                    height: 200,
                    child: Center(
                      child: Consumer<ModelIO>(
                          builder: (context, io, child) {
                            if (io.error) {
                              Provider.of<ModelIO>(context, listen: false).dismissError();
                              Future.delayed(Duration(seconds: 1)).then((value) {
                                _dialog.hide();
                                WidgetsBinding.instance.addPostFrameCallback((_) {
                                  _showAlertDialog(
                                      io.errorTitle, io.errorSubtitle);
                                });
                                Provider.of<ModelIO>(context, listen: false)
                                    .dismissError();
                              });

                              return Text("No faces found",style: TextStyle(
                                fontFamily: 'OpenSans',
                                fontSize: 20,
                              ),);
                            } else {
                              if (io.facesList.length == 0) {
                                _dialog.hide();
                                return Text("No faces found",style: TextStyle(
                                  fontFamily: 'OpenSans',
                                  fontSize: 20,
                                ),);
                              } else {
                                _dialog.hide();
                                return FacesList(facesList: io.facesList, isTablet: false);
                              }
                            }
                          }
                      ),
                    ),
                  ), // expanded
                ],),
            ),
          ],
        ),
      ),
    ),),
    );
  }

  Widget TabletLandscape(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Container(
          decoration: BoxDecoration(
            gradient: LinearGradient(
              begin: Alignment.topRight,
              end: Alignment.bottomLeft,
              colors: [Colors.blueAccent, Colors.black38])),
        child: Center(
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            mainAxisSize: MainAxisSize.max,
            children: <Widget> [
            Expanded(
              child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget> [
                SizedBox(
                  height: _height,
                  width: _width,
                  child: _picture == null
                      ? Center(child: new Text('Please select or take a photo!',style:TextStyle(
                    fontSize: 25,
                    fontFamily: 'Shrikhand',
                  ),))
                      : Center(
                    child: GestureDetector(
                      child: Image.file(_picture),
                      onTap: (() async {
                        Navigator.of(context).push(
                          MaterialPageRoute(
                            builder: (BuildContext context) {
                              return BigPicture(image: new Image.file(_picture).image);
                            },
                          ),
                        );
                      }),
                    ),
                  ),
                ),
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  mainAxisSize: MainAxisSize.max,
                  children: <Widget>[
                    IconButton(
                        iconSize: 90,
                        icon: Icon(Icons.add_a_photo),
                        onPressed: () {
                          _cameraButtonHandler();
                        }
                    ),
                    IconButton(
                        iconSize: 100,
                        icon: Icon(Icons.add_photo_alternate),
                        onPressed: () {
                          _galleryButtonHandler();
                        }
                    ),
                  ],
                ),
              ],
            ),), // Expanded
            Expanded(
              child: Container(
                height: MediaQuery.of(context).size.height,
                child: Center(
                  child: Consumer<ModelIO> (
                      builder: (context, io, child) {
                        if (io.error) {
                          Provider.of<ModelIO>(context, listen: false).dismissError();
                          Future.delayed(Duration(seconds:1)).then((value) {
                            _dialog.hide();

                            WidgetsBinding.instance.addPostFrameCallback((_) {
                              _showAlertDialog(io.errorTitle, io.errorSubtitle);
                            });
                            Provider.of<ModelIO>(context, listen: false).dismissError();
                          });

                          return Text("No faces found",style: TextStyle(
                            fontFamily: 'OpenSans',
                            fontSize: 30,
                          ),);
                        } else {
                          if(io.facesList.length == 0) {
                            _dialog.hide();
                            return Text("No faces found",style: TextStyle(
                              fontFamily: 'OpenSans',
                              fontSize: 30,
                            ),);
                          } else {
                            _dialog.hide();
                            return FacesList(facesList: io.facesList, isTablet: true);
                          }}
                      }
                  ),
                ),
              ),), // expanded
          ],
        ),
      ),
    ),),
    );
  }

  @override
  Widget build(BuildContext context) {
    _dialog = ProgressDialog(
      context,
      type: ProgressDialogType.Normal,
      isDismissible: false,
    );
    _dialog.style(
      message: 'Loading... Please wait',
      borderRadius: 10.0,
      backgroundColor: Colors.white,
      progressWidget: CircularProgressIndicator(),
      elevation: 10.0,
      insetAnimCurve: Curves.easeInOut,
      progress: 0.0,
      maxProgress: 100.0,
      progressTextStyle: TextStyle(
        color: Colors.black,
        fontSize: 13.0,
        fontWeight: FontWeight.w400,
      ),
      messageTextStyle: TextStyle(
        color: Colors.black,
        fontSize: 19.0,
        fontWeight: FontWeight.w600,
      ),
    );


    return LayoutBuilder(
        builder: (BuildContext context, BoxConstraints constraints) {
          if (constraints.smallest.longestSide < 800) {
            _height = 200; _width = 300;
            return OrientationBuilder(
                builder: (context, orientation) {
                  print("HEIGHT = ${_height} ;;; WIDTH = ${_width}");
                  return orientation == Orientation.portrait ? Portrait(context) : Landscape(context);
                }
            );
          } else {
            _height = 350; _width = 450;
            return OrientationBuilder(
                builder: (context, orientation) {
                  print("HEIGHT = ${_height} ;;; WIDTH = ${_width}");
                  return orientation == Orientation.portrait ? Portrait(context) : TabletLandscape(context);
                }
            );
          }
      }
    );
  }

  // Handlers
  void _cameraButtonHandler() {
    _drawImage(true);
  }

  void _galleryButtonHandler() {
    _drawImage(false);
  }

  void _drawImage(bool camera) async {
    var imSource;
    File pic = null;

    if (camera) {
      imSource = ImageSource.camera;
    } else {
      imSource = ImageSource.gallery;
    }

    pic = await ImagePicker.pickImage(
        source: imSource,
    );

    setState((){});
    // if the user does not takes or select a picture, app must rollback
    if (pic == null) return;
    _picture = pic;
    _dialog.update(
      message: "Loading... Please wait",
      progressWidget: CircularProgressIndicator(),
    );
    _dialog.show();
    print("MODEL CALLBACK ------------------------------------------------");
    Provider.of<ModelIO>(context, listen: false).uploadAndGetData(_picture);

  }
}