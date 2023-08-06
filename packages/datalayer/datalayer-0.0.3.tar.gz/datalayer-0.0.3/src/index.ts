import { JupyterFrontEnd, JupyterFrontEndPlugin } from '@jupyterlab/application';
import { ISettingRegistry } from '@jupyterlab/settingregistry';
import { MainAreaWidget, ICommandPalette } from '@jupyterlab/apputils';
import { ILauncher } from '@jupyterlab/launcher';
import { LabIcon } from '@jupyterlab/ui-components';
import { requestAPI } from './handler';
import { CounterWidget } from './widget';

import datalayerSvg from '../style/svg/datalayer.svg';

import '../style/index.css';

/**
 * The command IDs used by the plugin.
 */
namespace CommandIDs {
  export const create = 'create-datalayer-widget';
}

/**
 * Initialization data for the @datalayer/datalayer extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: '@datalayer/datalayer:plugin',
  autoStart: true,
  requires: [ICommandPalette],
  optional: [ISettingRegistry, ILauncher],
  activate: (
    app: JupyterFrontEnd,
    palette: ICommandPalette,
    settingRegistry: ISettingRegistry | null,
    launcher: ILauncher
  ) => {
    const { commands } = app;
    const command = CommandIDs.create;
    const datalayerIcon = new LabIcon({
      name: 'datalayer:icon',
      svgstr: datalayerSvg
    });
    commands.addCommand(command, {
      caption: 'Show Datalayer',
      label: 'Datalayer',
      icon: (args: any) => datalayerIcon,
      execute: () => {
        const content = new CounterWidget();
        const widget = new MainAreaWidget<CounterWidget>({ content });
        widget.title.label = 'Datalayer';
        widget.title.icon = datalayerIcon;
        app.shell.add(widget, 'main');
      }
    });
    const category = 'Datalayer';
    palette.addItem({ command, category });
    if (launcher) {
      launcher.add({
        command,
        category,
        rank: 1
      });
    }
    console.log('JupyterLab extension @datalayer/datalayer is activated!');
    if (settingRegistry) {
      settingRegistry
        .load(plugin.id)
        .then(settings => {
          console.log('@datalayer/datalayer settings loaded:', settings.composite);
        })
        .catch(reason => {
          console.error('Failed to load settings for @datalayer/datalayer.', reason);
        });
    }
    requestAPI<any>('get_config')
      .then(data => {
        console.log(data);
      })
      .catch(reason => {
        console.error(
          `The Jupyter Server extension appears to be missing.\n${reason}`
        );
      });
  }
};

export default plugin;
