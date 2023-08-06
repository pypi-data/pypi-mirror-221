import { createRoot } from 'react-dom/client';
import Clouder from './components/Clouder';

const root = createRoot(
  document.getElementById('root') as HTMLElement
);

root.render(<Clouder />);
