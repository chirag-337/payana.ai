import 'package:flutter/material.dart';
import '../core/theme/app_theme.dart';
import '../screens/home_screen.dart';

class PayanaApp extends StatelessWidget {
  const PayanaApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Payana.ai',
      debugShowCheckedModeBanner: false,
      theme: AppTheme.darkTheme,
      home: const HomeScreen(),
    );
  }
}

