<html data-theme="retro">
<head>
    <link href="https://cdn.jsdelivr.net/npm/daisyui@3.9.4/dist/full.css" rel="stylesheet" type="text/css" />
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/theme-change@2.0.2/index.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
    <link rel="icon" href="../k.png">
    <title>Ajouter un site</title>
</head>

<nav class="fixed top-0 left-0 z-20 rounded-lg m-2 navbar bg-base-200" style="width: -webkit-fill-available;">
  <div class="navbar-start">

    <div class="dropdown">
      <label tabindex="0" class="btn btn-ghost lg:hidden">
        <i class="fa-solid fa-bars"></i>
      </label>

      <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
        <li><a href="../">
            <i class="fa-solid fa-house"></i> Acceuil
          </a></li>
        <li><a href="">
            <i class="fa-solid fa-folder-plus"></i> Ajouter un serveur
          </a></li>
      </ul>

    </div>

    <div class="hidden lg:block">
      <ul class="menu menu-horizontal px-1">

        <li>
          <a href="../">
            <i class="fa-solid fa-house"></i> Acceuil
          </a>
        </li>
        <li>
          <a href="">
            <i class="fa-solid fa-folder-plus"></i> Ajouter un serveur
          </a>
        </li>

      </ul>
    </div>
  </div>
  <div class="navbar-center">
    <a class="btn btn-ghost normal-case text-xl">
      <img src="../title.png" class="h-10 w-auto">
    </a>
  </div>

  <div class="navbar-end">
      <label class="btn btn-ghost swap swap-rotate">

        <!-- this hidden checkbox controls the state -->
        <input type="checkbox" data-toggle-theme="retro,coffee" class="null">

        <!-- sun icon -->
        <i class="swap-on fa-solid fa-sun fa-xl"></i>

        <!-- moon icon -->
        <i class="swap-off fa-solid fa-moon fa-xl"></i>

      </label>
  </div>
</nav>
<!-- <div class="mt-32 flex content-center object-center justify-center">
<div class="mt-32 w-auto alert alert-error fixed top-0 z-20">
  <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
  <span>Impossible de créer des serveurs. Contacter <strong>@funasitien</strong> sur discord pour rajouter votre site.</span>
</div>
</div> -->
    <body>
        <div class="hero bg-base-100" style="height : 92vh;">
            <form method="post" action="account.php">
                <div class="hero-content flex-col lg:flex-row-reverse">
            
                <!-- <div class="text-center lg:text-left">
                    <h1 class="text-5xl font-bold">Login now!</h1>
                    <p class="py-6">Provident cupiditate voluptatem et in. Quaerat fugiat ut assumenda excepturi exercitationem quasi. In deleniti eaque aut repudiandae et a id nisi.</p>
                </div>-->

                    <div class="card flex-shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
                        <div class="card-body">
                            <div class="card-title">Données Facultatives</div>
                          <p>Ces données nous permettent de vous contacter quand votre site sera évalué.</p>
                        <div class="form-control">
                            <label class="label">
                                <span class="label-text">Email</span>
                            </label>
                            <input type="email" placeholder="funasitien@dreamclouds.fr" id="email" name="mail" class="input input-bordered" defaultValue="nuul@email.com" />
                        </div>
                        <div class="form-control">
                            <label class="label">
                                <span class="label-text">Discord</span>
                            </label>
                            <div class="join">
                                <a class="btn join-item">@</a>
                                <input type="text" placeholder="funasitien" id="discord" name="discord" class="input input-bordered join-item" defaultValue="@wumpus" />
                            </div>
                        </div>
                    </div>
                </div>

                <div class="divider divider-horizontal">PLUS</div>

                    <div class="card flex-shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
                        <div class="card-body">
                            <div class="card-title">Enregistrer votre serveur</div>
                                <div class="form-control">
                                    <label class="label">
                                        <span class="label-text">Adresse IP</span>
                                    </label>
                                    <input type="text" placeholder="172.16.4.10" id="ip" name="ip" class="input input-bordered" required />
                                </div>
                                <div class="form-control">
                                    <label class="label">
                                        <span class="label-text">Nom</span>
                                    </label>
                                    <input type="text" placeholder="Mon Site Web" id="nom" name="nom" class="input input-bordered" required />
                                </div>
                                <div class="form-control mt-6">
                                    <input  class="btn btn-primary" type="submit" value="Envoyer">
                                </div>
                            </div>
                        </div>
                    </div>
                </div> 
            </form> 
        </div>
    </body>
</html>

<footer class="footer items-center p-4 bg-base-300 text-accent-content">
  <a href="https://f.dreamclouds.fr" target="_blank">
  <aside class="items-center grid-flow-col btn btn-ghost">
    <svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" version="1.0" viewBox="0 0 606 606" class="fill-current"><path d="M358.5 87.7c-36.2 4.7-67 19.2-91.7 43.1l-7.7 7.5-6.3-2.6c-9.2-3.6-23.6-6.7-36.2-7.7-62.6-5.2-121.1 34.1-141.5 94.8-3.8 11.3-5.7 21.9-6.6 36.9l-.7 11.2-5.5 4.2c-13.5 10.4-29.8 31.1-37.4 47.4-13.2 28.1-16.6 61.3-9.3 91 11.8 48 51.3 87.5 99.3 99.4 18 4.5 18.3 4.5 145.8 2.5l120.3-1.8 6.9-12c22.4-39.3 122.2-234.6 135-264.4l5.3-12.4-.7-11.6c-.9-14.8-1.6-18.1-6.5-29.3-25.6-59.6-82.9-97.5-146.2-96.8-7.3.1-14.6.4-16.3.6zm43.2 44.8c47.3 7.4 77.7 39.4 80 84.1l.6 11.1-6.7 13.8c-7.1 14.8-22.6 44.8-66.3 128.3-15 28.8-32.9 63.5-39.7 77.1l-12.4 24.7-106.4 1.1c-59.5.6-109.7.6-114 .2-22.5-2.5-46.4-15.8-61-34-7.1-8.8-15.9-26.4-18.5-36.9-2.2-9.1-2.5-31.5-.4-40 5.9-24.9 21.2-47 40.6-58.7 7.7-4.7 10.1-6.6 12.8-9.9 2.1-2.7 2.2-3.8 2.2-24.4 0-20.9.1-21.7 2.9-30 8.9-26.7 25.3-46.1 49.1-58 12.5-6.2 22.9-9 36.6-9.7 19.1-1 32.9 2.3 51.4 12.2 16 8.6 20.2 7.7 31-6.6 18.9-24.9 45.8-41.1 75.5-45.4 10.9-1.6 28.5-1.2 42.7 1zM482.3 371.2l-25.2 49.3 23.7 46.7 23.7 46.8H560l-23.8-47.8-23.8-47.7 11.1-21.5c6-11.9 17.2-33.6 24.7-48.3l13.7-26.7h-54.4l-25.2 49.2z"/></svg>
    <p>Copyright © 2023 - All right reserved</p>
  </aside>
  </a>
  <nav class="grid-flow-col gap-4 md:place-self-center md:justify-self-end">
    <a class="" href="https://dsc.gg/drmcld" target="_blank">
      <i class="fa-brands fa-discord fa-xl"></i>
    </a>

    <a class="" href="https://www.kernacraft.studio" target="_blank">
      <i class="fa-solid fa-gamepad fa-xl"></i>
    </a> 

    <a class="" href="https://instagram.com/fdreamcloud" target="_blank">
      <i class="fa-brands fa-instagram fa-xl"></i>
    </a> 
  </nav>
</footer>