USE dibscheduler;

CREATE TABLE users (
    id char(36) PRIMARY KEY,
    name varchar(255) NOT NULL,
    mail varchar(255) NOT NULL UNIQUE,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NULL,
    deleted_at TIMESTAMP NULL
);

CREATE TABLE permission_users (
    id char(36) PRIMARY KEY,
    id_user char(36) NOT NULL,
    id_permission char(36) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NULL,
    deleted_at TIMESTAMP NULL
);

CREATE TABLE permission (
    id char(36) PRIMARY KEY,
    name varchar(255) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL,
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
    mail,
    created_at
)
VALUES (
    '69c11ffb-3244-45c6-a920-7ab7316658f6',
    'Bruno Oliveira',
    'bruoli3@gmail.com',
    now()
),
(
    '17868b01-a481-4654-a0e4-78170958adce',
    'Giovana de Moraes',
    'giovanamrufino@gmail.com',
    now()
)

INSERT INTO permission (
    id,
    name,
    created_at
)
VALUES (
    'a7880c74-8517-44a5-bdd5-02789b35ecd5',
    'admin',
    now()
),
(
    '30923a23-3644-43d6-bdad-b8ac3aa778e4',
    'secretary',
    now()
)

INSERT INTO permission_users (
    id,
    id_user,
    id_permission,
    created_at
)
VALUES (
    'e3bb0771-c05e-4f32-b765-5d44e1102457',
    '69c11ffb-3244-45c6-a920-7ab7316658f6',
    'a7880c74-8517-44a5-bdd5-02789b35ecd5',
    now()
),
(
    '82e54f2f-a875-4a16-a604-1704a09bf984',
    '17868b01-a481-4654-a0e4-78170958adce',
    '30923a23-3644-43d6-bdad-b8ac3aa778e4',
    now()
)
