create table public.places
(
    id                       serial                           not null
        primary key,
    poi_id                   varchar                           not null,
    name                     varchar                           not null,
    schema_url               varchar                           not null,
    website                  varchar,
    latitude                 double precision                  not null,
    longitude                double precision                  not null,
    updated_at             timestamp with time zone default now() not null,
    source_updated          date                              not null,
    constraint places_poi_id_uindex
        unique (poi_id)
);

alter table public.places
    owner to itinary;

create table public.places_to_classes
(
    id         bigserial        constraint places_to_classes_pk
            primary key,
    poi_id  varchar not null
        constraint places_fk
            references public.places(poi_id),
    classes_id integer not null
        constraint classes_fk
            references public.classes,
    created_at timestamp with time zone      default now() not null,
    updated_at timestamp with time zone default now() not null

);

alter table public.places_to_classes
    owner to itinary;

create table public.contacts
(
    id         serial
        constraint contacts_pk
            primary key,
    poi_id  varchar not null
        constraint contacts_places_id_fk
            references public.places(poi_id),
    schema_url varchar,
    type       varchar,
    phone      varchar,
    created_at timestamp with time zone      default now() not null,
    updated_at timestamp with time zone default now() not null
);

comment on column public.contacts.type is 'pour le moment en varchar, mais aprés ingestion on fera un enum';

alter table public.contacts
    owner to itinary;

create table public.descriptions
(
    id         bigserial
        constraint descriptions_pk
            primary key,
    poi_id  varchar not null
        constraint descriptions_places_id_fk
            references public.places(poi_id),
    content text,
    schema_url varchar,
    created_at timestamp with time zone      default now() not null,
    updated_at timestamp with time zone default now() not null,
    constraint descriptions_pk2
        unique (poi_id)
);

alter table public.descriptions
    owner to itinary;

create table public.addresses
(
    id         serial
        constraint addresses_pk
            primary key,
    poi_id  varchar not null
        constraint addresses_places_id_fk
            references public.places(poi_id),
    schema_url varchar not null,
    locality   varchar,
    zipcode    integer,
    street     varchar,
    created_at timestamp with time zone      default now() not null,
    updated_at timestamp with time zone default now() not null
);

alter table public.addresses
    owner to itinary;

create table public.openings
(
    id        bigserial
        constraint openings_pk
            primary key,
    poi_id varchar not null
        constraint openings_places_id_fk
            references public.places(poi_id),
    start_date    date,
    end_date   date,
    opens     time with time zone,
    closes    time with time zone,
    created_at timestamp with time zone      default now() not null,
    updated_at timestamp with time zone default now() not null
);

alter table public.openings
    owner to itinary;

