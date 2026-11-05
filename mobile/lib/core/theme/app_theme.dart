import 'package:flutter/material.dart';

class AppTheme {
  static final darkTheme = ThemeData(
    brightness: Brightness.dark,
    scaffoldBackgroundColor: const Color(0xFF0F172A),
    primaryColor: const Color(0xFF10B981),
    colorScheme: const ColorScheme.dark(
      primary: Color(0xFF10B981),
      secondary: Color(0xFF06B6D4),
      surface: Color(0xFF1E293B),
    ),
    fontFamily: 'Inter',
    useMaterial3: true,
  );
}

