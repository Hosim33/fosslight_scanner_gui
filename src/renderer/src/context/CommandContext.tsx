import { FC, ReactNode, createContext, useEffect, useState } from 'react';

export interface ICommandContext {
  analyzeCommandConfig: AnalyzeCommandConfig;
  compareCommandConfig: CompareCommandConfig;
  setAnalyzeCommandConfig: any;
  setCompareCommandConfig: any;
}

const CommandContext = createContext<ICommandContext | undefined>(undefined);

interface ICommandProviderProps {
  children: ReactNode;
}

export const CommandProvider: FC<ICommandProviderProps> = ({ children }) => {
  const [analyzeCommandConfig, setAnalyzeCommandConfig] = useState<AnalyzeCommandConfig>({
    outputFormat: 'excel'
  });
  const [compareCommandConfig, setCompareCommandConfig] = useState<CompareCommandConfig>({
    outputFormat: 'excel'
  });

  return (
    <CommandContext.Provider
      value={{
        analyzeCommandConfig,
        compareCommandConfig,
        setAnalyzeCommandConfig,
        setCompareCommandConfig
      }}
    >
      {children}
    </CommandContext.Provider>
  );
};

export default CommandContext;
