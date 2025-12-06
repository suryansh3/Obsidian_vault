# Create a wrapper script in your vault directory
# Save this as `runjava.sh` (Linux/Mac) or `runjava.bat` (Windows)

# For Windows (runjava.bat):
@echo off
javac Main.java 2>nul || (
    echo Compiling...
    javac Main.java
)
java Main