import time
from playwright.async_api import async_playwright
import parametros as p
import credenciales as c
import logging
import os

class ProbadorOrangeHRM:
    async def run(self, datos):
        # Seleccionar usuarios a actualizar
        lista_actualizaciones = datos[p.clave_prueba]
        # Cnfiguracion para logs y reportes
        self.configurar_logs()
        cont_correctos = 0
        cont_incorrectos = 0
        self.print_log_info('----------------INICIO PROCESO DE ACTUALIZACION DE USUARIOS----------------')
        async with async_playwright() as play:
            self.print_log_info('El proceso corre en segundo plano' if p.headless else 'El proceso corre en primer plano')
            browser = await play.chromium.launch(headless=p.headless)  # ver lo que ocurre
            page = await browser.new_page()
            # Abrir pagina
            await page.goto(p.url_orange_hrm, wait_until='networkidle')
            # Logeo
            await page.fill('input[name="username"]', c.user)
            await page.fill('input[name="password"]', c.password)
            await page.click('button[type="submit"]')
            error_locator = page.locator('text=Invalid credentials')
            try:
                await error_locator.wait_for(state="visible", timeout=5000)
                self.print_log_error(f'Las credenciales estan incorrectas')
            except Exception:
                self.print_log_info(f'Se tiene {len(lista_actualizaciones)} usuarios para actualizar')
                self.print_log_info(f'El usuario {c.user} inicio sesion')
                # Loop sobre json
                for index, dic in enumerate(lista_actualizaciones):
                    # Garantizar Admin
                    await page.click("span:has-text('Admin')")
                    # Editar usuario
                    selector = f'//div[@role="row" and .//div[@role="cell" and contains(normalize-space(.),"{dic["usuario_actual"]}")]]//i[contains(@class,"bi-pencil-fill")]'
                    try:
                        await page.click(selector)
                        if len(dic["usuario_nuevo"]) >= 5:
                            await page.wait_for_selector('//label[normalize-space(text())="Username"]', timeout=10000)
                            time.sleep(1)
                            await page.fill('//label[normalize-space(text())="Username"]/ancestor::div[contains(@class,"oxd-input-group")]//input', dic["usuario_nuevo"])
                            await page.click('button[type="submit"]')
                            await page.wait_for_selector('div.oxd-toast--success', timeout=10000)
                            self.print_log_info(f'{index + 1}. Se actualizo {dic["usuario_actual"]} por {dic["usuario_nuevo"]} correctamente')
                            cont_correctos += 1
                        else:
                            self.print_log_error(f'{index + 1}. {dic["usuario_nuevo"]} debe tener al menos 5 caracteres')
                            cont_incorrectos += 1
                    except Exception:
                        self.print_log_error(f'{index + 1}. No existe el username {dic["usuario_actual"]}')
                        cont_incorrectos += 1
            # Cerrar navegador
            await browser.close()
            self.print_log_info(f'Se actualizaron {cont_correctos} correctamente y fallaron {cont_incorrectos}')
            self.print_log_info('----------------FIN PROCESO DE ACTUALIZACION DE USUARIOS----------------')

    def configurar_logs(self):
        root_dir = os.path.dirname(os.path.abspath(__file__))
        log_path = os.path.join(root_dir, "mi_script.log")
        logging.basicConfig(
            filename='reporte_novedades.txt',
            filemode='a',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    def print_log_info(self, valor):
        logging.info(valor)
        print(valor)

    def print_log_error(self, valor):
        logging.error(valor)
        print(valor)