import { useState, useEffect } from 'react';
import { ThemeProvider, BaseStyles, Box } from '@primer/react';
import { UnderlineNav } from '@primer/react/drafts';
import { CloudIcon, CloudVirtualMachineIcon, KeyOutlineIcon } from '@datalayer/icons-react';
import { requestAPI } from '../handler';
import ClouderTab from './ClouderTab';
import KeysTab from './KeysTab';
import VirtualMachineTab from './VirtualMachineTab';

const Clouder = (): JSX.Element => {
  const [tab, setTab] = useState(1);
  const [version, setVersion] = useState('');
  useEffect(() => {
    requestAPI<any>('get_config')
    .then(data => {
      setVersion(data.version);
    })
    .catch(reason => {
      console.error(
        `The Jupyter Server clouder extension appears to be missing.\n${reason}`
      );
    });
  });
  return (
    <>
      <ThemeProvider>
        <BaseStyles>
          <Box style={{maxWidth: 700}}>
            <Box>
              <UnderlineNav>
                <UnderlineNav.Item aria-current="page" icon={CloudIcon} onSelect={e => {e.preventDefault(); setTab(1);}}>
                  Clouder
                </UnderlineNav.Item>
                <UnderlineNav.Item icon={KeyOutlineIcon} onSelect={e => {e.preventDefault(); setTab(2);}}>
                  Keys
                </UnderlineNav.Item>
                <UnderlineNav.Item icon={CloudVirtualMachineIcon} onSelect={e => {e.preventDefault(); setTab(3);}}>
                  Virtual Machines
                </UnderlineNav.Item>
              </UnderlineNav>
            </Box>
            <Box m={3}>
              {(tab === 1) && <ClouderTab version={version}/>}
              {(tab === 2) && <KeysTab/>}
              {(tab === 3) && <VirtualMachineTab/>}
            </Box>
          </Box>
        </BaseStyles>
      </ThemeProvider>
    </>
  );
};

export default Clouder;
