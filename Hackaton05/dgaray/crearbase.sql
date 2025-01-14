CREATE TABLE "orders" (
  "id" varchar PRIMARY KEY NOT NULL,
  "order_date" date NOT NULL,
  "ship_date" date NOT NULL,
  "customer_id" varchar NOT NULL,
  "ship_mode_id" int NOT NULL
);

CREATE TABLE "ship_mode" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY NOT NULL,
  "mode" varchar NOT NULL
);

CREATE TABLE "customers" (
  "id" varchar PRIMARY KEY NOT NULL,
  "name" varchar NOT NULL,
  "customer_segmet_id" int NOT NULL,
  "country" varchar DEFAULT 'United States',
  "city_id" int NOT NULL
);

CREATE TABLE "customer_segmet" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY NOT NULL,
  "name" varchar NOT NULL
);

CREATE TABLE "city" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY NOT NULL,
  "name" varchar NOT NULL
);

CREATE TABLE "state" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY NOT NULL,
  "name" varchar NOT NULL,
  "city_id" int NOT NULL
);

CREATE TABLE "postal_code" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY NOT NULL,
  "number" int NOT NULL,
  "state_id" int NOT NULL,
  "region_id" int NOT NULL
);

CREATE TABLE "region" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY NOT NULL,
  "name" varchar NOT NULL,
  "postal_code_id" int NOT NULL
);

CREATE TABLE "products_in_order" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY NOT NULL,
  "product_id" varchar NOT NULL,
  "order_id" varchar NOT NULL,
  "quantity" int DEFAULT 1
);

CREATE TABLE "products" (
  "id" varchar PRIMARY KEY NOT NULL,
  "name" varchar NOT NULL,
  "category_id" int NOT NULL
);

CREATE TABLE "categories" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY NOT NULL,
  "name" varchar NOT NULL
);

CREATE TABLE "sub_categories" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY NOT NULL,
  "name" varchar NOT NULL,
  "category_id" int NOT NULL
);

ALTER TABLE "orders" ADD FOREIGN KEY ("customer_id") REFERENCES "customers" ("id");

ALTER TABLE "customers" ADD FOREIGN KEY ("customer_segmet_id") REFERENCES "customer_segmet" ("id");

ALTER TABLE "customers" ADD FOREIGN KEY ("city_id") REFERENCES "city" ("id");

ALTER TABLE "state" ADD FOREIGN KEY ("city_id") REFERENCES "city" ("id");

ALTER TABLE "postal_code" ADD FOREIGN KEY ("state_id") REFERENCES "state" ("id");

ALTER TABLE "postal_code" ADD FOREIGN KEY ("region_id") REFERENCES "region" ("id");

ALTER TABLE "products_in_order" ADD FOREIGN KEY ("product_id") REFERENCES "products" ("id");

ALTER TABLE "products_in_order" ADD FOREIGN KEY ("order_id") REFERENCES "orders" ("id");

ALTER TABLE "products" ADD FOREIGN KEY ("category_id") REFERENCES "categories" ("id");

ALTER TABLE "orders" ADD FOREIGN KEY ("ship_mode_id") REFERENCES "ship_mode" ("id");

ALTER TABLE "sub_categories" ADD FOREIGN KEY ("category_id") REFERENCES "categories" ("id");