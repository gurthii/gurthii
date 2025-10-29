fun main(){
    val saraReview = CoffeeReview("Sara", "Loved it!", 5)
    val tobesReview = CoffeeReview("Tobes", "Was okay", 3)
    val hueyReview = CoffeeReview("Riley", "Sijapenda", 0)

    val somn: Int = null
    println(somn)

    println("${hueyReview.name}, ${hueyReview.comment}, ${hueyReview.stars}")
    println("${tobesReview.name}, ${tobesReview.comment}, ${tobesReview.stars}")
    println("${saraReview.name}, ${saraReview.comment}, ${saraReview.stars}")

}


class CoffeeReview (
    val name: String,
    val comment: String,
    val stars: Int
)
