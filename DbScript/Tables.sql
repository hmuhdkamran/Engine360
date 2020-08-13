--
-- PostgreSQL database dump
--

-- Dumped from database version 10.4
-- Dumped by pg_dump version 12.3

-- Started on 2020-08-13 11:38:40

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 71862)
-- Name: Role; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA "Role";


ALTER SCHEMA "Role" OWNER TO postgres;

SET default_tablespace = '';

--
-- TOC entry 198 (class 1259 OID 71873)
-- Name: Roles; Type: TABLE; Schema: Role; Owner: postgres
--

CREATE TABLE "Role"."Roles" (
    "RoleId" uuid NOT NULL,
    "ParentRoleId" uuid,
    "FullName" text NOT NULL,
    "Status" boolean NOT NULL
);


ALTER TABLE "Role"."Roles" OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 71895)
-- Name: RolesRoutesMap; Type: TABLE; Schema: Role; Owner: postgres
--

CREATE TABLE "Role"."RolesRoutesMap" (
    "RoleRouteMapId" uuid NOT NULL,
    "RoleId" uuid NOT NULL,
    "RouteId" uuid NOT NULL,
    "Status" boolean NOT NULL
);


ALTER TABLE "Role"."RolesRoutesMap" OWNER TO postgres;

--
-- TOC entry 199 (class 1259 OID 71883)
-- Name: Routes; Type: TABLE; Schema: Role; Owner: postgres
--

CREATE TABLE "Role"."Routes" (
    "RouteId" uuid NOT NULL,
    "RouteName" text NOT NULL,
    "DisplayName" text NOT NULL,
    "Status" boolean NOT NULL
);


ALTER TABLE "Role"."Routes" OWNER TO postgres;

--
-- TOC entry 197 (class 1259 OID 71863)
-- Name: Users; Type: TABLE; Schema: Role; Owner: postgres
--

CREATE TABLE "Role"."Users" (
    "UserId" uuid NOT NULL,
    "Username" text NOT NULL,
    "DisplayName" text NOT NULL,
    "Language" character varying(5) NOT NULL,
    "Password" text NOT NULL,
    "Salt" text NOT NULL,
    "Status" boolean
);


ALTER TABLE "Role"."Users" OWNER TO postgres;

--
-- TOC entry 201 (class 1259 OID 71912)
-- Name: UsersRolesMap; Type: TABLE; Schema: Role; Owner: postgres
--

CREATE TABLE "Role"."UsersRolesMap" (
    "UserRoleMapId" uuid NOT NULL,
    "UserId" uuid NOT NULL,
    "RoleRouteMapId" uuid NOT NULL,
    "Status" boolean NOT NULL
);


ALTER TABLE "Role"."UsersRolesMap" OWNER TO postgres;

--
-- TOC entry 2190 (class 0 OID 71873)
-- Dependencies: 198
-- Data for Name: Roles; Type: TABLE DATA; Schema: Role; Owner: postgres
--

COPY "Role"."Roles" ("RoleId", "ParentRoleId", "FullName", "Status") FROM stdin;
\.


--
-- TOC entry 2192 (class 0 OID 71895)
-- Dependencies: 200
-- Data for Name: RolesRoutesMap; Type: TABLE DATA; Schema: Role; Owner: postgres
--

COPY "Role"."RolesRoutesMap" ("RoleRouteMapId", "RoleId", "RouteId", "Status") FROM stdin;
\.


--
-- TOC entry 2191 (class 0 OID 71883)
-- Dependencies: 199
-- Data for Name: Routes; Type: TABLE DATA; Schema: Role; Owner: postgres
--

COPY "Role"."Routes" ("RouteId", "RouteName", "DisplayName", "Status") FROM stdin;
\.


--
-- TOC entry 2189 (class 0 OID 71863)
-- Dependencies: 197
-- Data for Name: Users; Type: TABLE DATA; Schema: Role; Owner: postgres
--

COPY "Role"."Users" ("UserId", "Username", "DisplayName", "Language", "Password", "Salt", "Status") FROM stdin;
\.


--
-- TOC entry 2193 (class 0 OID 71912)
-- Dependencies: 201
-- Data for Name: UsersRolesMap; Type: TABLE DATA; Schema: Role; Owner: postgres
--

COPY "Role"."UsersRolesMap" ("UserRoleMapId", "UserId", "RoleRouteMapId", "Status") FROM stdin;
\.


--
-- TOC entry 2057 (class 2606 OID 71899)
-- Name: RolesRoutesMap Pk_RolesRoutesMap_RoleRouteMapId; Type: CONSTRAINT; Schema: Role; Owner: postgres
--

ALTER TABLE ONLY "Role"."RolesRoutesMap"
    ADD CONSTRAINT "Pk_RolesRoutesMap_RoleRouteMapId" PRIMARY KEY ("RoleRouteMapId") WITH (fillfactor='80');


--
-- TOC entry 2047 (class 2606 OID 71880)
-- Name: Roles Pk_Roles_RoleId; Type: CONSTRAINT; Schema: Role; Owner: postgres
--

ALTER TABLE ONLY "Role"."Roles"
    ADD CONSTRAINT "Pk_Roles_RoleId" PRIMARY KEY ("RoleId") WITH (fillfactor='80');


--
-- TOC entry 2051 (class 2606 OID 71890)
-- Name: Routes Pk_Routes_RouteId; Type: CONSTRAINT; Schema: Role; Owner: postgres
--

ALTER TABLE ONLY "Role"."Routes"
    ADD CONSTRAINT "Pk_Routes_RouteId" PRIMARY KEY ("RouteId") WITH (fillfactor='80');


--
-- TOC entry 2061 (class 2606 OID 71916)
-- Name: UsersRolesMap Pk_UsersRolesMap_UserRoleMapId; Type: CONSTRAINT; Schema: Role; Owner: postgres
--

ALTER TABLE ONLY "Role"."UsersRolesMap"
    ADD CONSTRAINT "Pk_UsersRolesMap_UserRoleMapId" PRIMARY KEY ("UserRoleMapId") WITH (fillfactor='80');


--
-- TOC entry 2043 (class 2606 OID 71870)
-- Name: Users Pk_Users_UserID; Type: CONSTRAINT; Schema: Role; Owner: postgres
--

ALTER TABLE ONLY "Role"."Users"
    ADD CONSTRAINT "Pk_Users_UserID" PRIMARY KEY ("UserId") WITH (fillfactor='80');


--
-- TOC entry 2059 (class 2606 OID 71901)
-- Name: RolesRoutesMap Uk_RolesRoutesMap_RoleId_RouteId; Type: CONSTRAINT; Schema: Role; Owner: postgres
--

ALTER TABLE ONLY "Role"."RolesRoutesMap"
    ADD CONSTRAINT "Uk_RolesRoutesMap_RoleId_RouteId" UNIQUE ("RoleId", "RouteId") WITH (fillfactor='80');


--
-- TOC entry 2049 (class 2606 OID 71882)
-- Name: Roles Uk_Roles_FullName; Type: CONSTRAINT; Schema: Role; Owner: postgres
--

ALTER TABLE ONLY "Role"."Roles"
    ADD CONSTRAINT "Uk_Roles_FullName" UNIQUE ("FullName") WITH (fillfactor='80');


--
-- TOC entry 2053 (class 2606 OID 71894)
-- Name: Routes Uk_Routes_DisplayName; Type: CONSTRAINT; Schema: Role; Owner: postgres
--

ALTER TABLE ONLY "Role"."Routes"
    ADD CONSTRAINT "Uk_Routes_DisplayName" UNIQUE ("DisplayName") WITH (fillfactor='80');


--
-- TOC entry 2055 (class 2606 OID 71892)
-- Name: Routes Uk_Routes_RouteName; Type: CONSTRAINT; Schema: Role; Owner: postgres
--

ALTER TABLE ONLY "Role"."Routes"
    ADD CONSTRAINT "Uk_Routes_RouteName" UNIQUE ("RouteName") WITH (fillfactor='80');


--
-- TOC entry 2063 (class 2606 OID 71918)
-- Name: UsersRolesMap Uk_UsersRolesMap_UserId_RoleRouteMapId; Type: CONSTRAINT; Schema: Role; Owner: postgres
--

ALTER TABLE ONLY "Role"."UsersRolesMap"
    ADD CONSTRAINT "Uk_UsersRolesMap_UserId_RoleRouteMapId" UNIQUE ("UserId", "RoleRouteMapId") WITH (fillfactor='80');


--
-- TOC entry 2045 (class 2606 OID 71872)
-- Name: Users Uk_Users_Username; Type: CONSTRAINT; Schema: Role; Owner: postgres
--

ALTER TABLE ONLY "Role"."Users"
    ADD CONSTRAINT "Uk_Users_Username" UNIQUE ("Username") WITH (fillfactor='80');


--
-- TOC entry 2064 (class 2606 OID 71902)
-- Name: RolesRoutesMap Fk_RolesRoutesMap_RoleId; Type: FK CONSTRAINT; Schema: Role; Owner: postgres
--

ALTER TABLE ONLY "Role"."RolesRoutesMap"
    ADD CONSTRAINT "Fk_RolesRoutesMap_RoleId" FOREIGN KEY ("RoleId") REFERENCES "Role"."Roles"("RoleId") ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2065 (class 2606 OID 71907)
-- Name: RolesRoutesMap Fk_RolesRoutesMap_RouteId; Type: FK CONSTRAINT; Schema: Role; Owner: postgres
--

ALTER TABLE ONLY "Role"."RolesRoutesMap"
    ADD CONSTRAINT "Fk_RolesRoutesMap_RouteId" FOREIGN KEY ("RouteId") REFERENCES "Role"."Routes"("RouteId") ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2067 (class 2606 OID 71924)
-- Name: UsersRolesMap Fk_UsersRolesMap_RoleRouteMapId; Type: FK CONSTRAINT; Schema: Role; Owner: postgres
--

ALTER TABLE ONLY "Role"."UsersRolesMap"
    ADD CONSTRAINT "Fk_UsersRolesMap_RoleRouteMapId" FOREIGN KEY ("RoleRouteMapId") REFERENCES "Role"."RolesRoutesMap"("RoleRouteMapId") ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2066 (class 2606 OID 71919)
-- Name: UsersRolesMap Fk_UsersRolesMap_UserId; Type: FK CONSTRAINT; Schema: Role; Owner: postgres
--

ALTER TABLE ONLY "Role"."UsersRolesMap"
    ADD CONSTRAINT "Fk_UsersRolesMap_UserId" FOREIGN KEY ("UserId") REFERENCES "Role"."Users"("UserId") ON UPDATE CASCADE ON DELETE CASCADE;


-- Completed on 2020-08-13 11:38:40

--
-- PostgreSQL database dump complete
--

