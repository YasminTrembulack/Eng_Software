CREATE DATABASE IF NOT EXISTS `backend_development`;

USE `backend_development`;

CREATE TABLE IF NOT EXISTS `tasks` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `title` VARCHAR(255) NOT NULL,
    `description` TEXT,
    `status` ENUM('pending', 'done') NOT NULL DEFAULT 'pending',
    `priority` ENUM('low', 'medium', 'high') NOT NULL DEFAULT 'low',
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



-- -- Inseri alguns dados para visualização no front
INSERT INTO `tasks` (`title`, `description`, `status`, `priority`)
VALUES
('Configurar servidor', 'Instalar dependências e configurar ambiente inicial', 'pending', 'high'),
('Criar modelo de usuário', 'Definir campos e relacionamentos da tabela users', 'pending', 'medium'),
('Implementar autenticação', 'Adicionar login e registro com JWT', 'pending', 'high'),
('Testar API de tarefas', 'Escrever testes unitários e de integração', 'done', 'low'),
('Documentar endpoints', 'Criar documentação no Swagger/OpenAPI', 'pending', 'medium'),
('Criar página de login', 'Desenvolver interface para autenticação do usuário', 'pending', 'high'),
('Configurar CI/CD', 'Automatizar build e deploy com GitHub Actions', 'pending', 'high'),
('Ajustar layout responsivo', 'Corrigir CSS para melhor experiência em mobile', 'done', 'medium'),
('Escrever README', 'Adicionar instruções de instalação e uso no projeto', 'pending', 'low'),
('Revisar código', 'Fazer code review das últimas PRs enviadas', 'pending', 'medium');
