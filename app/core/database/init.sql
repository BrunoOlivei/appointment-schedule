/* POSTGRESQL */
CREATE TABLE users (
    id CHAR(36) PRIMARY KEY,
    name varchar(255) NOT NULL,
    mail varchar(255) NOT NULL UNIQUE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NULL,
    deleted_at TIMESTAMP NULL
);

CREATE TABLE permission_users (
    id CHAR(36) PRIMARY KEY,
    id_user CHAR(36) NOT NULL,
    id_permission CHAR(36) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NULL,
    deleted_at TIMESTAMP NULL
);

CREATE TABLE permission (
    id CHAR(36) PRIMARY KEY,
    name varchar(255) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NULL,
    deleted_at TIMESTAMP NULL
);

CREATE TABLE login_log (
    id CHAR(36) PRIMARY KEY,
    id_user CHAR(36) NOT NULL,
    login_date TIMESTAMP NOT NULL,
    logout_date TIMESTAMP NULL
);

ALTER TABLE permission_users ADD CONSTRAINT FK_permission_users_1
    FOREIGN KEY (id_user)
    REFERENCES users (id);
 
ALTER TABLE permission_users ADD CONSTRAINT FK_permission_users_2
    FOREIGN KEY (id_permission)
    REFERENCES permission (id);

ALTER TABLE login_log ADD CONSTRAINT FK_login_user_1
    FOREIGN KEY (id_user)
    REFERENCES users (id);

INSERT INTO users (
    id,
    name,
    mail
)
VALUES (
    '1353520d-83ad-472c-8c9c-ebb4000e3e54',
    'Bruno Oliveira',
    'bruoli3@gmail.com'
),
(
    'edefae26-09cb-4dd7-9dc3-24c679aadfbc',
    'Giovana de Moraes',
    'giovanamrufino@gmail.com'
);

INSERT INTO permission (
    id,
    name
)
VALUES (
    '4012eac2-5573-4d09-8ac2-6258da71f119',
    'admin'
),
(
    'f2e54fa0-cd2f-49ac-8054-bfc4c4e35f51',
    'secretary'
);
