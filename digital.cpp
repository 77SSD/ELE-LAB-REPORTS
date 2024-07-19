long long convert(int);
 {
  int n, bin;
  cout << "Enter a decimal number: ";
  cin >> n;
  bin = convert(n);
  cout << n << " in decimal = " << bin << " in binary" << endl ;
  return 0;
}