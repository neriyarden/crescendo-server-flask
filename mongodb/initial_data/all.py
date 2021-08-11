import datetime
from mongodb.models.tags import Tag
from mongodb.models.events import Event
from mongodb.models.users import User
from mongodb.models.requests import Request


"""Dummy data for the db"""

def insert_dummydata():
    Solo = Tag.create_tag('Solo')
    Acoustic = Tag.create_tag('Acoustic')
    Party = Tag.create_tag('Party')
    Intimate = Tag.create_tag('Intimate')
    Loud = Tag.create_tag('Loud')
    _18 = Tag.create_tag('18+')
    Kids = Tag.create_tag('Kids')
    Sitting = Tag.create_tag('Sitting')
    Standing = Tag.create_tag('Standing')
    Accessible = Tag.create_tag('Accessible')
    Electronic = Tag.create_tag('Electronic')
    Full_Band = Tag.create_tag('Full Band')


    jd = User.create_account('john doe', 'johndoe@gmail.com', 'jd123456!', False)
    sj = User.create_account('sarah j', 'sra@gmail.com', 'sj123456!', False)
    jm = User.create_account(
        name='Joe Mayor',
        email='joe_m@gmail.com',
        password='jm123456!',
        is_artist=True,
        img_url='img/artists/artists2.jpg',
        bio="Joe Mayor is an English funk and acid jazz band from London. Formed in 1992, they are fronted by vocalist Jay Kay, and were prominent in the London-based funk and acid jazz movement of the 1990s. The band's output blends their anything-goes approach with aggressive dance rhythms and 1970s influenced sounds. Their later releases drew from rock, disco, Electronic and Latin music genres. Lyrically, the group have addressed social and environmental justice. Kay has remained as the only original member through several line-up changes.",
        link_to_spotify="https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid?si=lZa0EhCnRIO7FhXDO-Wvkw&dl_branch=1",
        link_to_instagram="https://www.instagram.com/jamiroquaihq/",
        link_to_facebook="https://www.facebook.com/Jamiroquai",
        link_to_youtube="https://www.youtube.com/channel/UCd8wWXk6fSa8b8WaZbpWgvg",
    )
    an = User.create_account(
        name = 'Allóu Neder',
        email = 'allou_n@gmail.com',
        password = 'an123456!',
        is_artist = True,
        img_url = '/img/artists/artists3.jpg',
        bio = """Allóu Neder (born 15 June 1995) is an Australian singer-songwriter and multi-instrumentalist,[1] described as a \"one-person band\".[2] Sultana is best known for their 2016 single \"Jungle\", which was voted into third place in Triple J's Hottest 100 of 2016.
        The following year, Sultana had three songs voted into Triple J's Hottest 100 of 2017; \"Mystik\" at number 28, \"Murder to the Mind\" at number 43, and their Like a Version of \"Electric Feel\" at number 78.[3]
        Sultana grew up in Melbourne, and has been playing guitar from the age of three,[1] beginning a career in music through busking.[4] An active musician on Bandcamp since 2013,[5] Sultana's recordings were viewed millions of times on YouTube in 2016. Sultana's EP, Notion, was released on 23 September 2016, followed by a sold-out world tour in early 2017.""",
        link_to_spotify="https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid?si=lZa0EhCnRIO7FhXDO-Wvkw&dl_branch=1",
        link_to_instagram="https://www.instagram.com/jamiroquaihq/",
        link_to_facebook="https://www.facebook.com/Jamiroquai",
        link_to_youtube="https://www.youtube.com/channel/UCd8wWXk6fSa8b8WaZbpWgvg",
    )
    jb = User.create_account(
        name = 'Jamie Beerhouse',
        email = 'jamie_b@gmail.com',
        password = 'jb123456!',
        is_artist = True,
        img_url = '/img/artists/artists4.jpg',
        bio = """Jamie Beerhouse (born 15 June 1995) is an Australian singer-songwriter and multi-instrumentalist,[1] described as a \"one-person band\".[2] Sultana is best known for their 2016 single \"Jungle\", which was voted into third place in Triple J's Hottest 100 of 2016.
            The following year, Sultana had three songs voted into Triple J's Hottest 100 of 2017; \"Mystik\" at number 28, \"Murder to the Mind\" at number 43, and their Like a Version of \"Electric Feel\" at number 78.[3]
            Sultana grew up in Melbourne, and has been playing guitar from the age of three,[1] beginning a career in music through busking.[4] An active musician on Bandcamp since 2013,[5] Sultana's recordings were viewed millions of times on YouTube in 2016. Sultana's EP, Notion, was released on 23 September 2016, followed by a sold-out world tour in early 2017.""",
        link_to_spotify="https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid?si=lZa0EhCnRIO7FhXDO-Wvkw&dl_branch=1",
        link_to_instagram="https://www.instagram.com/jamiroquaihq/",
        link_to_facebook="https://www.facebook.com/Jamiroquai",
        link_to_youtube="https://www.youtube.com/channel/UCd8wWXk6fSa8b8WaZbpWgvg",
    )
    cj = User.create_account(
        name = 'Ctrl-J',
        email = 'ctrl_j@gmail.com',
        password = 'cj123456!',
        is_artist = True,
        img_url = '/img/artists/artists5.jpg',
        bio = """Ctrl-J (born 15 June 1995) is an Australian singer-songwriter and multi-instrumentalist,[1] described as a \"one-person band\".[2] Sultana is best known for their 2016 single \"Jungle\", which was voted into third place in Triple J's Hottest 100 of 2016.
            The following year, Sultana had three songs voted into Triple J's Hottest 100 of 2017; \"Mystik\" at number 28, \"Murder to the Mind\" at number 43, and their Like a Version of \"Electric Feel\" at number 78.[3]
            Sultana grew up in Melbourne, and has been playing guitar from the age of three,[1] beginning a career in music through busking.[4] An active musician on Bandcamp since 2013,[5] Sultana's recordings were viewed millions of times on YouTube in 2016. Sultana's EP, Notion, was released on 23 September 2016, followed by a sold-out world tour in early 2017.""",
        link_to_spotify="https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid?si=lZa0EhCnRIO7FhXDO-Wvkw&dl_branch=1",
        link_to_instagram="https://www.instagram.com/jamiroquaihq/",
        link_to_facebook="https://www.facebook.com/Jamiroquai",
        link_to_youtube="https://www.youtube.com/channel/UCd8wWXk6fSa8b8WaZbpWgvg",
    )
    hp = User.create_account(
        name = 'Hotplay',
        email = 'hotplay@gmail.com',
        password = 'hp1234561',
        is_artist = True,
        img_url = '/img/artists/artists6.jpg',
        bio = """Hotplay (born 15 June 1995) is an Australian singer-songwriter and multi-instrumentalist,[1] described as a \"one-person band\".[2] Sultana is best known for their 2016 single \"Jungle\", which was voted into third place in Triple J's Hottest 100 of 2016.
            The following year, Sultana had three songs voted into Triple J's Hottest 100 of 2017; \"Mystik\" at number 28, \"Murder to the Mind\" at number 43, and their Like a Version of \"Electric Feel\" at number 78.[3]
            Sultana grew up in Melbourne, and has been playing guitar from the age of three,[1] beginning a career in music through busking.[4] An active musician on Bandcamp since 2013,[5] Sultana's recordings were viewed millions of times on YouTube in 2016. Sultana's EP, Notion, was released on 23 September 2016, followed by a sold-out world tour in early 2017.""",
        link_to_spotify="https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid?si=lZa0EhCnRIO7FhXDO-Wvkw&dl_branch=1",
        link_to_instagram="https://www.instagram.com/jamiroquaihq/",
        link_to_facebook="https://www.facebook.com/Jamiroquai",
        link_to_youtube="https://www.youtube.com/channel/UCd8wWXk6fSa8b8WaZbpWgvg",
    )
    df = User.create_account(
        name = 'Dust Funk',
        email = 'dust_f@gmail.com',
        password = 'df123456!',
        is_artist = True,
        img_url = '/img/artists/artists7.jpg',
        bio = """Dust Funk (born 15 June 1995) is an Australian singer-songwriter and multi-instrumentalist,[1] described as a \"one-person band\".[2] Sultana is best known for their 2016 single \"Jungle\", which was voted into third place in Triple J's Hottest 100 of 2016.
            The following year, Sultana had three songs voted into Triple J's Hottest 100 of 2017; \"Mystik\" at number 28, \"Murder to the Mind\" at number 43, and their Like a Version of \"Electric Feel\" at number 78.[3]
            Sultana grew up in Melbourne, and has been playing guitar from the age of three,[1] beginning a career in music through busking.[4] An active musician on Bandcamp since 2013,[5] Sultana's recordings were viewed millions of times on YouTube in 2016. Sultana's EP, Notion, was released on 23 September 2016, followed by a sold-out world tour in early 2017.""",
        link_to_spotify="https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid?si=lZa0EhCnRIO7FhXDO-Wvkw&dl_branch=1",
        link_to_instagram="https://www.instagram.com/jamiroquaihq/",
        link_to_facebook="https://www.facebook.com/Jamiroquai",
        link_to_youtube="https://www.youtube.com/channel/UCd8wWXk6fSa8b8WaZbpWgvg",
    )
    ds = User.create_account(
        name = 'Diet Spraits',
        email = 'diet_s@gmail.com',
        password = 'ds123456!',
        is_artist = True,
        img_url = '/img/artists/artists8.jpg',
        bio = """Diet Spraits (born 15 June 1995) is an Australian singer-songwriter and multi-instrumentalist,[1] described as a \"one-person band\".[2] Sultana is best known for their 2016 single \"Jungle\", which was voted into third place in Triple J's Hottest 100 of 2016.
            The following year, Sultana had three songs voted into Triple J's Hottest 100 of 2017; \"Mystik\" at number 28, \"Murder to the Mind\" at number 43, and their Like a Version of \"Electric Feel\" at number 78.[3]
            Sultana grew up in Melbourne, and has been playing guitar from the age of three,[1] beginning a career in music through busking.[4] An active musician on Bandcamp since 2013,[5] Sultana's recordings were viewed millions of times on YouTube in 2016. Sultana's EP, Notion, was released on 23 September 2016, followed by a sold-out world tour in early 2017.""",
        link_to_spotify="https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid?si=lZa0EhCnRIO7FhXDO-Wvkw&dl_branch=1",
        link_to_instagram="https://www.instagram.com/jamiroquaihq/",
        link_to_facebook="https://www.facebook.com/Jamiroquai",
        link_to_youtube="https://www.youtube.com/channel/UCd8wWXk6fSa8b8WaZbpWgvg",
    )
    pl = User.create_account(
        name = 'Poo Lighters',
        email = 'poo_l@gmail.com',
        password = 'pl123456!',
        is_artist = True,
        img_url = '/img/artists/artists9.jpg',
        bio = """Poo Lighters (born 15 June 1995) is an Australian singer-songwriter and multi-instrumentalist,[1] described as a \"one-person band\".[2] Sultana is best known for their 2016 single \"Jungle\", which was voted into third place in Triple J's Hottest 100 of 2016.
            The following year, Sultana had three songs voted into Triple J's Hottest 100 of 2017; \"Mystik\" at number 28, \"Murder to the Mind\" at number 43, and their Like a Version of \"Electric Feel\" at number 78.[3]
            Sultana grew up in Melbourne, and has been playing guitar from the age of three,[1] beginning a career in music through busking.[4] An active musician on Bandcamp since 2013,[5] Sultana's recordings were viewed millions of times on YouTube in 2016. Sultana's EP, Notion, was released on 23 September 2016, followed by a sold-out world tour in early 2017.""",
        link_to_spotify="https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid?si=lZa0EhCnRIO7FhXDO-Wvkw&dl_branch=1",
        link_to_instagram="https://www.instagram.com/jamiroquaihq/",
        link_to_facebook="https://www.facebook.com/Jamiroquai",
        link_to_youtube="https://www.youtube.com/channel/UCd8wWXk6fSa8b8WaZbpWgvg",
    )
    fd = User.create_account(
        name = 'Fool Drunk',
        email = 'fool_d@gmail.com',
        password = 'fd123456!',
        is_artist = True,
        img_url = '/img/artists/artists10.jpg',
        bio = """Fool Drunk (born 15 June 1995) is an Australian singer-songwriter and multi-instrumentalist,[1] described as a \"one-person band\".[2] Sultana is best known for their 2016 single \"Jungle\", which was voted into third place in Triple J's Hottest 100 of 2016.
            The following year, Sultana had three songs voted into Triple J's Hottest 100 of 2017; \"Mystik\" at number 28, \"Murder to the Mind\" at number 43, and their Like a Version of \"Electric Feel\" at number 78.[3]
            Sultana grew up in Melbourne, and has been playing guitar from the age of three,[1] beginning a career in music through busking.[4] An active musician on Bandcamp since 2013,[5] Sultana's recordings were viewed millions of times on YouTube in 2016. Sultana's EP, Notion, was released on 23 September 2016, followed by a sold-out world tour in early 2017.""",
        link_to_spotify="https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid?si=lZa0EhCnRIO7FhXDO-Wvkw&dl_branch=1",
        link_to_instagram="https://www.instagram.com/jamiroquaihq/",
        link_to_facebook="https://www.facebook.com/Jamiroquai",
        link_to_youtube="https://www.youtube.com/channel/UCd8wWXk6fSa8b8WaZbpWgvg",
    )
    dc = User.create_account(
        name = 'Danny Cravitz',
        email = 'danny_c@gmail.com',
        password = 'dc123456!',
        is_artist = True,
        img_url = '/img/artists/artists11.jpg',
        bio = """Danny Cravitz (born 15 June 1995) is an Australian singer-songwriter and multi-instrumentalist,[1] described as a \"one-person band\".[2] Sultana is best known for their 2016 single \"Jungle\", which was voted into third place in Triple J's Hottest 100 of 2016.
            The following year, Sultana had three songs voted into Triple J's Hottest 100 of 2017; \"Mystik\" at number 28, \"Murder to the Mind\" at number 43, and their Like a Version of \"Electric Feel\" at number 78.[3]
            Sultana grew up in Melbourne, and has been playing guitar from the age of three,[1] beginning a career in music through busking.[4] An active musician on Bandcamp since 2013,[5] Sultana's recordings were viewed millions of times on YouTube in 2016. Sultana's EP, Notion, was released on 23 September 2016, followed by a sold-out world tour in early 2017.""",
        link_to_spotify="https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid?si=lZa0EhCnRIO7FhXDO-Wvkw&dl_branch=1",
        link_to_instagram="https://www.instagram.com/jamiroquaihq/",
        link_to_facebook="https://www.facebook.com/Jamiroquai",
        link_to_youtube="https://www.youtube.com/channel/UCd8wWXk6fSa8b8WaZbpWgvg",
    )
    no = User.create_account(
        name = 'Neil Old',
        email = 'neil_o@gmail.com',
        password = 'no123456!',
        is_artist = True,
        img_url = '/img/artists/artists12.jpg',
        bio = """Neil Old (born 15 June 1995) is an Australian singer-songwriter and multi-instrumentalist,[1] described as a \"one-person band\".[2] Sultana is best known for their 2016 single \"Jungle\", which was voted into third place in Triple J's Hottest 100 of 2016.
            The following year, Sultana had three songs voted into Triple J's Hottest 100 of 2017; \"Mystik\" at number 28, \"Murder to the Mind\" at number 43, and their Like a Version of \"Electric Feel\" at number 78.[3]
            Sultana grew up in Melbourne, and has been playing guitar from the age of three,[1] beginning a career in music through busking.[4] An active musician on Bandcamp since 2013,[5] Sultana's recordings were viewed millions of times on YouTube in 2016. Sultana's EP, Notion, was released on 23 September 2016, followed by a sold-out world tour in early 2017.""",
        link_to_spotify="https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid?si=lZa0EhCnRIO7FhXDO-Wvkw&dl_branch=1",
        link_to_instagram="https://www.instagram.com/jamiroquaihq/",
        link_to_facebook="https://www.facebook.com/Jamiroquai",
        link_to_youtube="https://www.youtube.com/channel/UCd8wWXk6fSa8b8WaZbpWgvg",
    )
    lf = User.create_account(
        name = 'Link Froyd',
        email = 'link_f@gmail.com',
        password = 'lf123456!',
        is_artist = True,
        img_url = '/img/artists/artists13.jpg',
        bio = """Link Froyd (born 15 June 1995) is an Australian singer-songwriter and multi-instrumentalist,[1] described as a \"one-person band\".[2] Sultana is best known for their 2016 single \"Jungle\", which was voted into third place in Triple J's Hottest 100 of 2016.
            The following year, Sultana had three songs voted into Triple J's Hottest 100 of 2017; \"Mystik\" at number 28, \"Murder to the Mind\" at number 43, and their Like a Version of \"Electric Feel\" at number 78.[3]
            Sultana grew up in Melbourne, and has been playing guitar from the age of three,[1] beginning a career in music through busking.[4] An active musician on Bandcamp since 2013,[5] Sultana's recordings were viewed millions of times on YouTube in 2016. Sultana's EP, Notion, was released on 23 September 2016, followed by a sold-out world tour in early 2017.""",
        link_to_spotify="https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid?si=lZa0EhCnRIO7FhXDO-Wvkw&dl_branch=1",
        link_to_instagram="https://www.instagram.com/jamiroquaihq/",
        link_to_facebook="https://www.facebook.com/Jamiroquai",
        link_to_youtube="https://www.youtube.com/channel/UCd8wWXk6fSa8b8WaZbpWgvg",
    )
    bb = User.create_account(
        name = 'The Blueberries',
        email = 'the_b@gmail.com',
        password = 'tb123456!',
        is_artist = True,
        img_url = '/img/artists/artists14.jpg',
        bio = """The Blueberries (born 15 June 1995) is an Australian singer-songwriter and multi-instrumentalist,[1] described as a \"one-person band\".[2] Sultana is best known for their 2016 single \"Jungle\", which was voted into third place in Triple J's Hottest 100 of 2016.
            The following year, Sultana had three songs voted into Triple J's Hottest 100 of 2017; \"Mystik\" at number 28, \"Murder to the Mind\" at number 43, and their Like a Version of \"Electric Feel\" at number 78.[3]
            Sultana grew up in Melbourne, and has been playing guitar from the age of three,[1] beginning a career in music through busking.[4] An active musician on Bandcamp since 2013,[5] Sultana's recordings were viewed millions of times on YouTube in 2016. Sultana's EP, Notion, was released on 23 September 2016, followed by a sold-out world tour in early 2017.""",
        link_to_spotify="https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid?si=lZa0EhCnRIO7FhXDO-Wvkw&dl_branch=1",
        link_to_instagram="https://www.instagram.com/jamiroquaihq/",
        link_to_facebook="https://www.facebook.com/Jamiroquai",
        link_to_youtube="https://www.youtube.com/channel/UCd8wWXk6fSa8b8WaZbpWgvg",
    )
    em = User.create_account(
        name = 'Eli Markyahu',
        email = 'eli_m@gmail.com',
        password = 'em123456!',
        is_artist = True,
        img_url = '/img/artists/artists15.jpg',
        bio = """Eli Markyahu (born 15 June 1995) is an Australian singer-songwriter and multi-instrumentalist,[1] described as a \"one-person band\".[2] Sultana is best known for their 2016 single \"Jungle\", which was voted into third place in Triple J's Hottest 100 of 2016.
            The following year, Sultana had three songs voted into Triple J's Hottest 100 of 2017; \"Mystik\" at number 28, \"Murder to the Mind\" at number 43, and their Like a Version of \"Electric Feel\" at number 78.[3]
            Sultana grew up in Melbourne, and has been playing guitar from the age of three,[1] beginning a career in music through busking.[4] An active musician on Bandcamp since 2013,[5] Sultana's recordings were viewed millions of times on YouTube in 2016. Sultana's EP, Notion, was released on 23 September 2016, followed by a sold-out world tour in early 2017.""",
        link_to_spotify="https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid?si=lZa0EhCnRIO7FhXDO-Wvkw&dl_branch=1",
        link_to_instagram="https://www.instagram.com/jamiroquaihq/",
        link_to_facebook="https://www.facebook.com/Jamiroquai",
        link_to_youtube="https://www.youtube.com/channel/UCd8wWXk6fSa8b8WaZbpWgvg",
    )
    _312 = User.create_account(
        name = '312',
        email = '312@gmail.com',
        password = 'to123456!',
        is_artist = True,
        img_url = '/img/artists/artists16.jpg',
        bio = """312 (born 15 June 1995) is an Australian singer-songwriter and multi-instrumentalist,[1] described as a \"one-person band\".[2] Sultana is best known for their 2016 single \"Jungle\", which was voted into third place in Triple J's Hottest 100 of 2016.
            The following year, Sultana had three songs voted into Triple J's Hottest 100 of 2017; \"Mystik\" at number 28, \"Murder to the Mind\" at number 43, and their Like a Version of \"Electric Feel\" at number 78.[3]
            Sultana grew up in Melbourne, and has been playing guitar from the age of three,[1] beginning a career in music through busking.[4] An active musician on Bandcamp since 2013,[5] Sultana's recordings were viewed millions of times on YouTube in 2016. Sultana's EP, Notion, was released on 23 September 2016, followed by a sold-out world tour in early 2017.""",
        link_to_spotify="https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid?si=lZa0EhCnRIO7FhXDO-Wvkw&dl_branch=1",
        link_to_instagram="https://www.instagram.com/jamiroquaihq/",
        link_to_facebook="https://www.facebook.com/Jamiroquai",
        link_to_youtube="https://www.youtube.com/channel/UCd8wWXk6fSa8b8WaZbpWgvg",
    )
    mh = User.create_account(
        name = 'M-hmm',
        email = 'm_h@gmail.com',
        password = 'mh123456!',
        is_artist = True,
        img_url = '/img/artists/artists17.jpg',
        bio = """M-hmm (born 15 June 1995) is an Australian singer-songwriter and multi-instrumentalist,[1] described as a \"one-person band\".[2] Sultana is best known for their 2016 single \"Jungle\", which was voted into third place in Triple J's Hottest 100 of 2016.
            The following year, Sultana had three songs voted into Triple J's Hottest 100 of 2017; \"Mystik\" at number 28, \"Murder to the Mind\" at number 43, and their Like a Version of \"Electric Feel\" at number 78.[3]
            Sultana grew up in Melbourne, and has been playing guitar from the age of three,[1] beginning a career in music through busking.[4] An active musician on Bandcamp since 2013,[5] Sultana's recordings were viewed millions of times on YouTube in 2016. Sultana's EP, Notion, was released on 23 September 2016, followed by a sold-out world tour in early 2017.""",
        link_to_spotify="https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid?si=lZa0EhCnRIO7FhXDO-Wvkw&dl_branch=1",
        link_to_instagram="https://www.instagram.com/jamiroquaihq/",
        link_to_facebook="https://www.facebook.com/Jamiroquai",
        link_to_youtube="https://www.youtube.com/channel/UCd8wWXk6fSa8b8WaZbpWgvg",
    )
    ob = User.create_account(
        name = 'Obelix',
        email = 'obelix@gmail.com',
        password = 'ob123456!',
        is_artist = True,
        img_url = '/img/artists/artists18.jpg',
        bio = """Obelix (born 15 June 1995) is an Australian singer-songwriter and multi-instrumentalist,[1] described as a \"one-person band\".[2] Sultana is best known for their 2016 single \"Jungle\", which was voted into third place in Triple J's Hottest 100 of 2016.
            The following year, Sultana had three songs voted into Triple J's Hottest 100 of 2017; \"Mystik\" at number 28, \"Murder to the Mind\" at number 43, and their Like a Version of \"Electric Feel\" at number 78.[3]
            Sultana grew up in Melbourne, and has been playing guitar from the age of three,[1] beginning a career in music through busking.[4] An active musician on Bandcamp since 2013,[5] Sultana's recordings were viewed millions of times on YouTube in 2016. Sultana's EP, Notion, was released on 23 September 2016, followed by a sold-out world tour in early 2017.""",
        link_to_spotify="https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid?si=lZa0EhCnRIO7FhXDO-Wvkw&dl_branch=1",
        link_to_instagram="https://www.instagram.com/jamiroquaihq/",
        link_to_facebook="https://www.facebook.com/Jamiroquai",
        link_to_youtube="https://www.youtube.com/channel/UCd8wWXk6fSa8b8WaZbpWgvg",
    )
    vs = User.create_account(
        name = 'Videoslave',
        email = 'video_s@gmail.com',
        password = 'vs123456!',
        is_artist = True,
        img_url = '/img/artists/artists19.jpg',
        bio = """Videoslave (born 15 June 1995) is an Australian singer-songwriter and multi-instrumentalist,[1] described as a \"one-person band\".[2] Sultana is best known for their 2016 single \"Jungle\", which was voted into third place in Triple J's Hottest 100 of 2016.
            The following year, Sultana had three songs voted into Triple J's Hottest 100 of 2017; \"Mystik\" at number 28, \"Murder to the Mind\" at number 43, and their Like a Version of \"Electric Feel\" at number 78.[3]
            Sultana grew up in Melbourne, and has been playing guitar from the age of three,[1] beginning a career in music through busking.[4] An active musician on Bandcamp since 2013,[5] Sultana's recordings were viewed millions of times on YouTube in 2016. Sultana's EP, Notion, was released on 23 September 2016, followed by a sold-out world tour in early 2017.""",
        link_to_spotify="https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid?si=lZa0EhCnRIO7FhXDO-Wvkw&dl_branch=1",
        link_to_instagram="https://www.instagram.com/jamiroquaihq/",
        link_to_facebook="https://www.facebook.com/Jamiroquai",
        link_to_youtube="https://www.youtube.com/channel/UCd8wWXk6fSa8b8WaZbpWgvg",
    )
    ax = User.create_account(
        name = 'Avi Xi',
        email = 'avi_x@gmail.com',
        password = 'ax123456!',
        is_artist = True,
        img_url = '/img/artists/artists20.jpg',
        bio = """Avi Xi (born 15 June 1995) is an Australian singer-songwriter and multi-instrumentalist,[1] described as a \"one-person band\".[2] Sultana is best known for their 2016 single \"Jungle\", which was voted into third place in Triple J's Hottest 100 of 2016.
            The following year, Sultana had three songs voted into Triple J's Hottest 100 of 2017; \"Mystik\" at number 28, \"Murder to the Mind\" at number 43, and their Like a Version of \"Electric Feel\" at number 78.[3]
            Sultana grew up in Melbourne, and has been playing guitar from the age of three,[1] beginning a career in music through busking.[4] An active musician on Bandcamp since 2013,[5] Sultana's recordings were viewed millions of times on YouTube in 2016. Sultana's EP, Notion, was released on 23 September 2016, followed by a sold-out world tour in early 2017.""",
        link_to_spotify="https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid?si=lZa0EhCnRIO7FhXDO-Wvkw&dl_branch=1",
        link_to_instagram="https://www.instagram.com/jamiroquaihq/",
        link_to_facebook="https://www.facebook.com/Jamiroquai",
        link_to_youtube="https://www.youtube.com/channel/UCd8wWXk6fSa8b8WaZbpWgvg",
    )
    bp = User.create_account(
        name = 'Bruna Pluto',
        email = 'bruna_p@gmail.com',
        password = 'bp123456!',
        is_artist = True,
        img_url = '/img/artists/artists21.jpg',
        bio = """Bruna Pluto (born 15 June 1995) is an Australian singer-songwriter and multi-instrumentalist,[1] described as a \"one-person band\".[2] Sultana is best known for their 2016 single \"Jungle\", which was voted into third place in Triple J's Hottest 100 of 2016.
            The following year, Sultana had three songs voted into Triple J's Hottest 100 of 2017; \"Mystik\" at number 28, \"Murder to the Mind\" at number 43, and their Like a Version of \"Electric Feel\" at number 78.[3]
            Sultana grew up in Melbourne, and has been playing guitar from the age of three,[1] beginning a career in music through busking.[4] An active musician on Bandcamp since 2013,[5] Sultana's recordings were viewed millions of times on YouTube in 2016. Sultana's EP, Notion, was released on 23 September 2016, followed by a sold-out world tour in early 2017.""",
        link_to_spotify="https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid?si=lZa0EhCnRIO7FhXDO-Wvkw&dl_branch=1",
        link_to_instagram="https://www.instagram.com/jamiroquaihq/",
        link_to_facebook="https://www.facebook.com/Jamiroquai",
        link_to_youtube="https://www.youtube.com/channel/UCd8wWXk6fSa8b8WaZbpWgvg",
    )
    qol = User.create_account(
        name = 'Queens Of Lea',
        email = 'queens_o@gmail.com',
        password = 'qo123456!',
        is_artist = True,
        img_url = '/img/artists/artists22.jpg',
        bio = """Queens Of Lea (born 15 June 1995) is an Australian singer-songwriter and multi-instrumentalist,[1] described as a \"one-person band\".[2] Sultana is best known for their 2016 single \"Jungle\", which was voted into third place in Triple J's Hottest 100 of 2016.
            The following year, Sultana had three songs voted into Triple J's Hottest 100 of 2017; \"Mystik\" at number 28, \"Murder to the Mind\" at number 43, and their Like a Version of \"Electric Feel\" at number 78.[3]
            Sultana grew up in Melbourne, and has been playing guitar from the age of three,[1] beginning a career in music through busking.[4] An active musician on Bandcamp since 2013,[5] Sultana's recordings were viewed millions of times on YouTube in 2016. Sultana's EP, Notion, was released on 23 September 2016, followed by a sold-out world tour in early 2017.""",
        link_to_spotify="https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid?si=lZa0EhCnRIO7FhXDO-Wvkw&dl_branch=1",
        link_to_instagram="https://www.instagram.com/jamiroquaihq/",
        link_to_facebook="https://www.facebook.com/Jamiroquai",
        link_to_youtube="https://www.youtube.com/channel/UCd8wWXk6fSa8b8WaZbpWgvg",
    )
    ka = User.create_account(
        name = 'Karpada Arnevet',
        email = 'karpada_a@gmail.com',
        password = 'ka123456!',
        is_artist = True,
        img_url = '/img/artists/artists23.jpg',
        bio = """Karpada Arnevet (born 15 June 1995) is an Australian singer-songwriter and multi-instrumentalist,[1] described as a \"one-person band\".[2] Sultana is best known for their 2016 single \"Jungle\", which was voted into third place in Triple J's Hottest 100 of 2016.
            The following year, Sultana had three songs voted into Triple J's Hottest 100 of 2017; \"Mystik\" at number 28, \"Murder to the Mind\" at number 43, and their Like a Version of \"Electric Feel\" at number 78.[3]
            Sultana grew up in Melbourne, and has been playing guitar from the age of three,[1] beginning a career in music through busking.[4] An active musician on Bandcamp since 2013,[5] Sultana's recordings were viewed millions of times on YouTube in 2016. Sultana's EP, Notion, was released on 23 September 2016, followed by a sold-out world tour in early 2017.""",
        link_to_spotify="https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid?si=lZa0EhCnRIO7FhXDO-Wvkw&dl_branch=1",
        link_to_instagram="https://www.instagram.com/jamiroquaihq/",
        link_to_facebook="https://www.facebook.com/Jamiroquai",
        link_to_youtube="https://www.youtube.com/channel/UCd8wWXk6fSa8b8WaZbpWgvg",
    )
    yv = User.create_account(
        name = 'Yoni Ver',
        email = 'yoni_v@gmail.com',
        password = 'yv123456!',
        is_artist = True,
        img_url = '/img/artists/artists24.jpg',
        bio = """Yoni Ver (born 15 June 1995) is an Australian singer-songwriter and multi-instrumentalist,[1] described as a \"one-person band\".[2] Sultana is best known for their 2016 single \"Jungle\", which was voted into third place in Triple J's Hottest 100 of 2016.
            The following year, Sultana had three songs voted into Triple J's Hottest 100 of 2017; \"Mystik\" at number 28, \"Murder to the Mind\" at number 43, and their Like a Version of \"Electric Feel\" at number 78.[3]
            Sultana grew up in Melbourne, and has been playing guitar from the age of three,[1] beginning a career in music through busking.[4] An active musician on Bandcamp since 2013,[5] Sultana's recordings were viewed millions of times on YouTube in 2016. Sultana's EP, Notion, was released on 23 September 2016, followed by a sold-out world tour in early 2017.""",
        link_to_spotify="https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid?si=lZa0EhCnRIO7FhXDO-Wvkw&dl_branch=1",
        link_to_instagram="https://www.instagram.com/jamiroquaihq/",
        link_to_facebook="https://www.facebook.com/Jamiroquai",
        link_to_youtube="https://www.youtube.com/channel/UCd8wWXk6fSa8b8WaZbpWgvg",
    )


    Event.create_event(
        artist_id=jm,
        tour='Joe Mayer World Tour',
        duration=120,
        venue='Zappa Haifa',
        city='Haifa',
        description='wow amazing cool',
        img_url='/img/events/live1.jpg',
        ticketseller_url='https://www.eventim.co.il/',
        date=datetime.date(2021, 8, 7).strftime("%d/%m/%Y"),
        time=datetime.time(23).strftime("%H:%M:%S"),
        tags=[Solo, Loud, Accessible, Standing]
    )
    Event.create_event(
        artist_id=jm,
        tour='Joe Mayer World Tour',
        duration=120,
        venue='Barby',
        city='Tel Aviv',
        description='wow amazing cool',
        img_url='/img/events/live1.jpg',
        ticketseller_url='https://www.eventim.co.il/',
        date=datetime.date(2021, 8, 20).strftime("%d/%m/%Y"),
        time=datetime.time(22).strftime("%H:%M:%S"),
        tags=[Solo, Acoustic, Electronic, Sitting]
    )
    Event.create_event(
        artist_id=jm,
        tour='Joe Mayer World Tour',
        duration=120,
        venue='הצוללת הצהובה',
        city='Jerusalem',
        description='wow amazing cool',
        img_url='/img/events/live1.jpg',
        ticketseller_url='https://www.eventim.co.il/',
        date=datetime.date(2021, 9, 21).strftime("%d/%m/%Y"),
        time=datetime.time(22).strftime("%H:%M:%S"),
        tags=[Full_Band, Kids, Intimate, Party],
        featured=True
    )
    Event.create_event(
        artist_id=an,
        tour='Allóu Neder Israel Tour',
        duration=120,
        venue='Zappa Haifa',
        city='Haifa',
        description='wow amazing cool',
        img_url='/img/events/live2.jpg',
        ticketseller_url='https://www.eventim.co.il/',
        date=datetime.date(2021, 9, 16).strftime("%d/%m/%Y"),
        time=datetime.time(22).strftime("%H:%M:%S"),
        tags=[Solo, Kids, Sitting, Party]
    )
    Event.create_event(
        artist_id=an,
        tour='Allóu Neder Israel Tour',
        duration=90,
        venue='Barby',
        city='Tel Aviv',
        description='wow amazing cool',
        img_url='/img/events/live2.jpg',
        ticketseller_url='https://www.eventim.co.il/',
        date=datetime.date(2021, 7, 25).strftime("%d/%m/%Y"),
        time=datetime.time(20).strftime("%H:%M:%S"),
        tags=[Loud, Party, _18, Full_Band, Standing]
    )

    req1 = Request.create_request(
        artist_id = jm,
        tour = 'Joe Mayor World Tour',
        city = 'Afula',
        cap = 1200

    )
    req2 = Request.create_request(
        artist_id = an,
        tour = 'Allóu Neder Israel Tour',
        city = 'Jerusalem',
        cap = 1400
    )

    Request.cast_vote(req1, jd)
    Request.cast_vote(req2, jd)
    Request.cast_vote(req1, bb)
    Request.cast_vote(req1, lf)
    Request.cast_vote(req2, lf)
    Request.cast_vote(req1, no)
    Request.cast_vote(req2, no)
    Request.cast_vote(req1, dc)
    Request.cast_vote(req1, fd)
    Request.cast_vote(req1, pl)
    Request.cast_vote(req2, pl)
    Request.cast_vote(req1, ds)
    Request.cast_vote(req1, df)
    Request.cast_vote(req1, hp)
    Request.cast_vote(req2, hp)
    Request.cast_vote(req1, cj)
    Request.cast_vote(req1, jb)
    Request.cast_vote(req2, jb)
    Request.cast_vote(req1, an)
    Request.cast_vote(req1, jm)
    Request.cast_vote(req2, jm)