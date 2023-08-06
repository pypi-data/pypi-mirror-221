import { ReactWidget } from '@jupyterlab/apputils';
import Clouder from './components/Clouder';

export class CounterWidget extends ReactWidget {
  constructor() {
    super();
    this.addClass('dla-Container');
  }

  render(): JSX.Element {
    return <Clouder />;
  }
}
