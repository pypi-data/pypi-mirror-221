import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { IThemeManager } from '@jupyterlab/apputils';
import { ITranslator } from '@jupyterlab/translation';

/**
 * Initialization data for the jupyterlab-theme-onedark extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'jupyterlab-theme-onedark:plugin',
  description: 'A JupyterLab extension.',
  autoStart: true,
  requires: [IThemeManager, ITranslator],
  activate: (
    app: JupyterFrontEnd,
    manager: IThemeManager,
    translator: ITranslator,
  ) => {

    console.log('JupyterLab extension jupyterlab-theme-onedark is activated!');
    const style = 'mytheme/index.css';
    const trans = translator.load('jupyterlab');

    manager.register({
      name: 'jupyterlab-theme-onedark',
      isLight: false,
      displayName: trans.__('jupyterlab-theme-onedark'),
      themeScrollbars: true,
      load: () => manager.loadCSS(style),
      unload: () => Promise.resolve(undefined)
    });
  }
};

export default plugin;
