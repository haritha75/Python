# class level attibutes that are share  all instances of a class if you change value it is visible to the all the object of type
class Point:
    count = 0  # This is a class attribute like static vairble in java without object we can access

    def __init__(self, x, y):
        self.x = x  # This is an instance attribute
        self.y = y  # This is an instance attribute
        Point.count += 1  # Incrementing class attribute count

# Creating instances of Point
point1 = Point(3, 5)
print("Total number of points created:", point1.count)

point2 = Point(7, 9)
print("Total number of points created:", point1.count)

# Accessing instance attributes
print("Point 1 coordinates:", point1.x, point1.y)
print("Point 2 coordinates:", point2.x, point2.y)
Point.count = 12 # we can change like this also

# Accessing class attribute
print("Total number of points created:", Point.count)
print("Total number of points created:", point1.count)




# in java
# public class Point {
#     // Instance variables
#     private int x;
#     private int y;

#     // Constructor
#     public Point(int x, int y) {
#         this.x = x;
#         this.y = y;
#     }

#     // Method to access instance variables
#     public void printCoordinates() {
#         System.out.println("x = " + x + ", y = " + y);
#     }

#     public static void main(String[] args) {
#         // Creating an instance of Point
#         Point point = new Point(3, 5);

#         // Accessing instance variables from outside the class
#         System.out.println("Coordinates of the point:");
#         point.printCoordinates();
#     }
# }
