CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER
);

CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "username" varchar,
  "password" varchar,
  "is_staff" bit
);

CREATE TABLE "RareUsers" (
  "id" INTEGER PRIMARY KEY,
  "bio" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit,
  "user_id" INTEGER
);

CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  "ended_on" date
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  "created_on" datetime
);

CREATE TABLE "Reaction" (
  "id" INTEGER PRIMARY KEY,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY,
  "user_id" INTEGER,
  "post_id" INTEGER,
  "reaction_id" INTEGER
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY,
  "tag_id" INTEGER,
  "post_id" INTEGER
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY,
  "label" varchar
);

SELECT * FROM Users

DELETE FROM Users

