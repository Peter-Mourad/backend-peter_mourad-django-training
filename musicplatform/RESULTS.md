# 1- create some artists

    -Queries
        from artists.models import Artist
        a1 = Artist(stage_name="Amr Diab", social_link="instagram.com/amrdiab")
        a2 = Artist(stage_name="Tamer Hosny", social_link="instagram.com/tamerhosny")
        a3 = Artist(stage_name="Eminem", social_link="instagram.com/eminem")
    -Results
        a1.save()
        a2.save()
        a3.save()

# 2- list down all artists

    -Queries
        for artist in Artist.objects.all().values():
            print(artist)
    -Results
        {'stage_name': 'Amr Diab', 'social_link': 'instagram.com/amrdiab'}
        {'stage_name': 'Eminem', 'social_link': 'instagram.com/eminem'}
        {'stage_name': 'Tamer Hosny', 'social_link': 'instagram.com/tamerhosny'}

# 3- list down all artists sorted by name

    -Queries
        for artist in Artist.objects.all().values().order_by('stage_name'):
            print(artist)
    -Results
        {'stage_name': 'Amr Diab', 'social_link': 'instagram.com/amrdiab'}
        {'stage_name': 'Eminem', 'social_link': 'instagram.com/eminem'}
        {'stage_name': 'Tamer Hosny', 'social_link': 'instagram.com/tamerhosny'}

# 4- list down all artists whose name starts with 'a'

    -Queries
        for artist in Artist.objects.all().filter(stage_name\_\_istartswith='a').values():
            print(artist)
    -Results
        {'stage_name': 'Amr Diab', 'social_link': 'instagram.com/amrdiab'}

# 5- in 2 different ways, create some albums and assign them to any artists

    -Queries
        from albums.models import Album
        from django.utils import timezone
        -first way
            artist1 = Artist.objects.get(stage_name='Amr Diab')
            artist2 = Artist.objects.get(stage_name='Eminem')
            Album.objects.create(artist_name=artist1, released_at='2021-12-11', cost=220.5)
            Album.objects.create(artist_name=artist2, released_at='2011-12-11', cost=220.5)
        -second way
            artist1.album_set.create(released_at='2021-12-11', cost=2000)
            artist2.album_set.create(released_at='2011-12-11', cost=3000)

# 6- get the latest released album

    -Queries
        Album.objects.all().order_by('-released_at').values()[0]
    -Results
        {'album_id': 11, 'artist_name_id': 'Eminem', 'name': 'New Album', 'created_at': datetime.datetime(2022, 10, 16, 13, 0, 49, 252047, tzinfo=datetime.timezone.utc), 'released_at': datetime.datetime(2022, 10, 16, 13, 0, 49, 252047, tzinfo=datetime.timezone.utc), 'cost': Decimal('3000.00')}

# 7- get all albums released before today

    -Queries
        for album in Album.objects.all().filter(released_at__lt = datetime.now().date()).values():
            print(album)
    -Results
        {'album_id': 8, 'artist_name_id': 'Amr Diab', 'name': 'New Album', 'created_at': datetime.datetime(2022, 10, 16, 12, 11, 47, 942800, tzinfo=datetime.timezone.utc), 'released_at': datetime.datetime(2021, 12, 12, 0, 0, tzinfo=datetime.timezone.utc), 'cost': Decimal('1300.00')}
        {'album_id': 9, 'artist_name_id': 'Amr Diab', 'name': 'New Album', 'created_at': datetime.datetime(2022, 10, 16, 12, 25, 55, 442916, tzinfo=datetime.timezone.utc), 'released_at': datetime.datetime(2021, 3, 2, 0, 0, tzinfo=datetime.timezone.utc), 'cost': Decimal('1300.00')}

# 8- get all albums released today or before but not after today

    -Queries
        for album in Album.objects.all().filter(released_at__lte = datetime.now().date() + timedelta(days=1)).values():
            print(album)
    -Results
        {'album_id': 6, 'artist_name_id': 'Eminem', 'name': 'New Album', 'created_at': datetime.datetime(2022, 10, 16, 10, 29, 37, 25818, tzinfo=datetime.timezone.utc), 'released_at': datetime.datetime(2022, 10, 16, 10, 29, 37, 24822, tzinfo=datetime.timezone.utc), 'cost': Decimal('230.50')}
        {'album_id': 8, 'artist_name_id': 'Amr Diab', 'name': 'New Album', 'created_at': datetime.datetime(2022, 10, 16, 12, 11, 47, 942800, tzinfo=datetime.timezone.utc), 'released_at': datetime.datetime(2021, 12, 12, 0, 0, tzinfo=datetime.timezone.utc), 'cost': Decimal('1300.00')}
        {'album_id': 9, 'artist_name_id': 'Amr Diab', 'name': 'New Album', 'created_at': datetime.datetime(2022, 10, 16, 12, 25, 55, 442916, tzinfo=datetime.timezone.utc), 'released_at': datetime.datetime(2021, 3, 2, 0, 0, tzinfo=datetime.timezone.utc), 'cost': Decimal('1300.00')}

# 9- count the total number of albums

    -Queries
        Album.objects.all().count()
    -Results
        7

# 10- in 2 different ways, for each artist, list down all of his/her albums

    -First way
        -Queries
            for artist in Artist.objects.all():
                print(artist.album_set.all().values())
    -Second way
        -Queries
            for artist in Artist.objects.all().values():
                print(Album.objects.filter(artist_name=artist['stage_name']).values())
    -Results
        <QuerySet [{'album_id': 5, 'artist_name_id': 'Amr Diab', 'name': 'New Album', 'created_at': datetime.datetime(2022, 10, 16, 10, 27, 36,
        995509, tzinfo=datetime.timezone.utc), 'released_at': datetime.datetime(2022, 10, 16, 10, 27, 36, 995509, tzinfo=datetime.timezone.utc), 'cost': Decimal('220.50')}, {'album_id': 8, 'artist_name_id': 'Amr Diab', 'name': 'New Album', 'created_at': datetime.datetime(2022, 10, 16, 12, 11, 47, 942800, tzinfo=datetime.timezone.utc), 'released_at': datetime.datetime(2021, 12, 12, 0, 0, tzinfo=datetime.timezone.utc), 'cost': Decimal('1300.00')}, {'album_id': 9, 'artist_name_id': 'Amr Diab', 'name': 'New Album', 'created_at': datetime.datetime(2022, 10, 16, 12, 25, 55, 442916, tzinfo=datetime.timezone.utc), 'released_at': datetime.datetime(2021, 3, 2, 0, 0, tzinfo=datetime.timezone.utc), 'cost': Decimal('1300.00')}]>
        <QuerySet [{'album_id': 6, 'artist_name_id': 'Eminem', 'name': 'New Album', 'created_at': datetime.datetime(2022, 10, 16, 10, 29, 37, 25818, tzinfo=datetime.timezone.utc), 'released_at': datetime.datetime(2022, 10, 16, 10, 29, 37, 24822, tzinfo=datetime.timezone.utc), 'cost': Decimal('230.50')}, {'album_id': 11, 'artist_name_id': 'Eminem', 'name': 'New Album', 'created_at': datetime.datetime(2022, 10, 16, 13, 0, 49, 252047, tzinfo=datetime.timezone.utc), 'released_at': datetime.datetime(2022, 10, 16, 13, 0, 49, 252047, tzinfo=datetime.timezone.utc),
        'cost': Decimal('3000.00')}]>

# 11- list down all albums ordered by cost then by name

    -Queries
        for album in Album.objects.all().order_by('cost', 'name').values():
            print(album)
    -Results
        {'album_id': 5, 'artist_name_id': 'Amr Diab', 'name': 'New Album', 'created_at': datetime.datetime(2022, 10, 16, 10, 27, 36, 995509, tzinfo=datetime.timezone.utc), 'released_at': datetime.datetime(2022, 10, 16, 10, 27, 36, 995509, tzinfo=datetime.timezone.utc), 'cost': Decimal('220.50')}
        {'album_id': 6, 'artist_name_id': 'Eminem', 'name': 'New Album', 'created_at': datetime.datetime(2022, 10, 16, 10, 29, 37, 25818, tzinfo=datetime.timezone.utc), 'released_at': datetime.datetime(2022, 10, 16, 10, 29, 37, 24822, tzinfo=datetime.timezone.utc), 'cost': Decimal('230.50')}
        {'album_id': 9, 'artist_name_id': 'Amr Diab', 'name': 'New Album', 'created_at': datetime.datetime(2022, 10, 16, 12, 25, 55, 442916, tzinfo=datetime.timezone.utc), 'released_at': datetime.datetime(2021, 3, 2, 0, 0, tzinfo=datetime.timezone.utc), 'cost': Decimal('1300.00')}
        {'album_id': 8, 'artist_name_id': 'Amr Diab', 'name': 'New Album', 'created_at': datetime.datetime(2022, 10, 16, 12, 11, 47, 942800, tzinfo=datetime.timezone.utc), 'released_at': datetime.datetime(2021, 12, 12, 0, 0, tzinfo=datetime.timezone.utc), 'cost': Decimal('1300.00')}
