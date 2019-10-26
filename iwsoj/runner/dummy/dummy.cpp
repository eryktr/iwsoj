#include <iostream>
#include <cmath>

struct Point
{
    double x, y, z;
    Point(double x, double y, double z): x(x), y(y), z(z) {}
};

double sq(double x) {
    return x*x;
}

double dist(const Point& p1, const Point& p2)
{
    return sqrt((sq(p1.x - p2.x) + sq(p1.y - p2.y) + sq(p1.z - p2.z)));
}

int main() {
    const Point &p1 = Point(0, 0, 0);
    const Point &p2 = Point(0, 0, 0);
    double d = dist(p1, p2);
    std::cout << "Distance from p1 and p2 is " << d << std::endl;
}
