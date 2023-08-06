import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { IThemeManager } from '@jupyterlab/apputils';
import { ITranslator } from '@jupyterlab/translation';

/**
 * Initialization data for the jupyterlab-extension-theme-onedark extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'jupyterlab-extension-theme-onedark:plugin',
  description: 'A JupyterLab extension theme as vscode onedark',
  autoStart: true,
  requires: [IThemeManager, ITranslator],
  activate: (
    app: JupyterFrontEnd,
    manager: IThemeManager,
    translator: ITranslator,

  ) => {
    console.log('JupyterLab extension jupyterlab-extension-theme-onedark is activated!');
    const style = 'jupyterlab-extension-theme-onedark/index.css';
    const trans = translator.load('jupyterlab');

    manager.register({
      name: 'jupyterlab-extension-theme-onedark',
      isLight: true,
      displayName: trans.__('JupyterLab OneDark'),
      load: () => manager.loadCSS(style),
      unload: () => Promise.resolve(undefined)
    });
  }
};

export default plugin;
