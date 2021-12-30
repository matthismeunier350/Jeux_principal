import pygame



class Dialogs:

    x_position = 60
    y_position = 470

    def __init__(self):
        self.box = pygame.image.load('dialogs/dialog_box.png')
        self.box = pygame.transform.scale(self.box,(700, 100))
        self.texts = ["Bonjour bienvenue dans ce monde, ", "je vais te poser trois questions", "tu dois y repondre bien", "","",""]
        self.text1 = ["","","", "question1","question 2","question3"]
        self.text_reponse = ["Gagne", "Perdu"]
        self.text_index = 0
        self.font = pygame.font.Font('dialogs/dialog_font.ttf', 18)
        self.lire = False
        self.text_reponse_vrai = False
        self.reponse1 = False
        self.text_reponse_faux = False




    def execute(self):
        if self.lire:
            self.text_suivant()
        else:
            self.lire = True
            self.text_index = 0


    def affichage(self, screen):
        if self.lire:
            screen.blit(self.box,(self.x_position, self.y_position))
            text = self.font.render(self.texts[self.text_index], False, (0, 0, 0))
            text1 = self.font.render(self.text1[self.text_index], False, (0, 0, 0))
            screen.blit(text, (self.x_position+60, self.y_position+30))
            screen.blit(text1, (self.x_position + 60, self.y_position + 60))

            if self.text_reponse_vrai == True:
                text_reponse_vrai= self.font.render(self.text_reponse[0], False, (0, 0, 0))
                screen.blit(text_reponse_vrai, (self.x_position + 200, self.y_position + 60))
            if self.text_reponse_faux == True:
                text_reponse_faux= self.font.render(self.text_reponse[1], False, (0, 0, 0))
                screen.blit(text_reponse_faux, (self.x_position + 200, self.y_position + 60))

    def text_suivant(self):
        self.text_index += 1

        if self.text_index >=len(self.texts):
            self.lire = False

    def touche_reponse1(self):
        pressed = pygame.key.get_pressed()
        if self.lire == True:

            self.reponse1 = True
            if pressed[pygame.K_z] and self.reponse1 == True :
                self.text_reponse_vrai = True
            if pressed[pygame.K_e] and self.reponse1 == True:
                self.text_reponse_faux = True









