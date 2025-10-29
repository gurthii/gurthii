fun main(){
    // Accessing the classes
    val breed: doggoBreeds = doggoBreeds.REX
    println(describe(breed))

    val doggo: doggoBreeds = doggoBreeds.MUTINA
    println(describe(doggo))
}

// Enumeration class for when you want to limit the number of possible values
enum class doggoBreeds {
    MUTINA,
    BOSCO,
    REX
}

// when statements used on enum entries ensures all possible values in class are exhaustively addressed
// an optional else statement may be added if your variable/object wasn't assigned any enum entry
fun describe(whatBreed: doggoBreeds) = when (whatBreed) {
    doggoBreeds.MUTINA -> "This is a Mutina"
    doggoBreeds.BOSCO -> "A Bosco doggo"
    // doggoBreeds.REX -> "A Vintage Rex"
    else -> "Unknown breed"
}

