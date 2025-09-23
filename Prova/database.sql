CREATE DATABASE IF NOT EXISTS cinema;

USE cinema;

CREATE TABLE IF NOT EXISTS cinema_ingressos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_filme VARCHAR(255) NOT NULL,
    genero VARCHAR(100),
    sessoes VARCHAR(100),
    nome_cliente VARCHAR(255),
    assento VARCHAR(20),
    data_filme DATETIME
);


-- -- Inseri alguns dados para visualização no front

-- INSERT INTO cinema_ingressos (nome_filme, genero, sessoes, nome_cliente, assento, data_filme)
-- VALUES
-- ('Avatar 2', 'Ficção Científica', 'Sala 1 - 19h', 'João Silva', 'A10', '2025-09-25 19:00:00'),
-- ('Avatar 2', 'Ficção Científica', 'Sala 1 - 19h', 'Maria Souza', 'A11', '2025-09-25 19:00:00'),
-- ('Oppenheimer', 'Drama', 'Sala 2 - 20h', 'Carlos Pereira', 'B05', '2025-09-25 20:00:00'),
-- ('Oppenheimer', 'Drama', 'Sala 2 - 20h', 'Ana Costa', 'B06', '2025-09-25 20:00:00'),
-- ('Barbie', 'Comédia', 'Sala 3 - 18h', 'Fernanda Lima', 'C01', '2025-09-25 18:00:00'),
-- ('Barbie', 'Comédia', 'Sala 3 - 18h', 'Rafael Gomes', 'C02', '2025-09-25 18:00:00'),
-- ('Homem-Aranha: Sem Volta para Casa', 'Ação', 'Sala 4 - 21h', 'Lucas Andrade', 'D15', '2025-09-25 21:00:00'),
-- ('Homem-Aranha: Sem Volta para Casa', 'Ação', 'Sala 4 - 21h', 'Juliana Torres', 'D16', '2025-09-25 21:00:00'),
-- ('Procurando Nemo', 'Animação', 'Sala 5 - 16h', 'Pedro Martins', 'E08', '2025-09-25 16:00:00'),
-- ('Procurando Nemo', 'Animação', 'Sala 5 - 16h', 'Isabela Rocha', 'E09', '2025-09-25 16:00:00');