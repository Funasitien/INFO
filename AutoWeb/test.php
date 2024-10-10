<!DOCTYPE html>
<html>
    <head>
        <title>Un formulaire</title>
        <meta charset="utf-8">
    </head>

    <body>
        <h1>Un formulaire</h1>
        <form method="get" action="traitement.php">
            <label for="nom">Nom</label>
            <input type="text" name="nom" value="" id="nom">
            <label for="prenom">Prénom</label>
            <input type="text" name="prenom" value="" id="prenom">
            <input type="submit" value="Envoyer">
        </form>
    </body>
</html>

<h1>Traitement du formulaire</h1>
<p>Bonjour <?php echo $_GET['prenom']; ?> <?php echo $_GET['nom']; ?>, votre formulaire a bien été traité.</p>
